"""Physical checks against numerical integration, not just formula duplication."""
import json
from pathlib import Path
import unittest

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
NB = json.loads((ROOT / "notebooks/01_sampling_resolution.ipynb").read_text())
MODEL = next(c["source"] for c in NB["cells"] if "model" in c["metadata"].get("tags", []))
if isinstance(MODEL, list):
    MODEL = "".join(MODEL)
NS = {"np": np, "brentq": brentq}
exec(MODEL, NS)


class ImagingPhysicsTests(unittest.TestCase):
    def test_gaussian_convolution_and_pixel_integration(self):
        # Independent numerical convolution of the object with a Gaussian LSF,
        # followed by integration over a pixel. Includes a negative sinc lobe.
        for f, sigma, pitch, phase in [(1, .04, .1, 35), (3, .02, .25, 0),
                                       (3, .1, .5, 70), (8, .01, .05, 180)]:
            x, samples = NS["sample_detector"](f, sigma, pitch, phase)
            def optical_at(position):
                return quad(lambda z: (.5 * (1 + .9*np.cos(
                    2*np.pi*f*(position-sigma*z) + np.deg2rad(phase))))
                    * np.exp(-z*z/2)/np.sqrt(2*np.pi), -10, 10,
                    epsabs=1e-11)[0]
            for i in [0, 3, len(x)-1]:
                expected = quad(optical_at, x[i]-pitch/2, x[i]+pitch/2,
                                epsabs=1e-10)[0] / pitch
                self.assertAlmostEqual(samples[i], expected, places=9)

    def test_alias_frequency_and_fit(self):
        m = NS["measurements"](3, .02, .25, 35)
        self.assertAlmostEqual(m["alias"], 1)
        contrast, coefficients = m["fit"]
        self.assertAlmostEqual(contrast, .9*m["pre_mtf"], places=12)
        x = m["x"]
        reconstructed = (coefficients[0] + coefficients[1]*np.cos(2*np.pi*x)
                         + coefficients[2]*np.sin(2*np.pi*x))
        np.testing.assert_allclose(reconstructed, m["values"], atol=1e-13)

    def test_nyquist_phase_degeneracy_and_dc(self):
        zero = NS["measurements"](2, .02, .25, 0)
        shifted = NS["measurements"](2, .02, .25, 90)
        np.testing.assert_allclose(zero["values"], .5, atol=1e-14)
        self.assertGreater(shifted["sample_range_contrast"], .5)
        self.assertIsNone(zero["fit"])
        self.assertIsNone(shifted["fit"])
        dc_alias = NS["measurements"](4, 0, .25, 0)
        self.assertEqual(dc_alias["alias"], 0)
        self.assertIsNone(dc_alias["fit"])

    def test_zero_blur_and_aperture_zero(self):
        np.testing.assert_allclose(NS["optical_otf"](np.arange(20), 0), 1)
        for pitch in NS["PITCHES_MM"]:
            x, samples = NS["sample_detector"](1/pitch, 0, pitch, 75)
            np.testing.assert_allclose(samples, .5, atol=1e-14)
            self.assertAlmostEqual(len(x)*pitch, 8)

    def test_mtf50_and_blur_bandwidth(self):
        frequencies = [NS["mtf50"](s, .1) for s in [0, .04, .25, .5]]
        self.assertTrue(all(a > b for a, b in zip(frequencies, frequencies[1:])))
        for sigma, f50 in zip([0, .04, .25, .5], frequencies):
            self.assertAlmostEqual(NS["presampling_otf"](f50, sigma, .1), .5)

    def test_bounds_and_alias_band_over_control_domain(self):
        for pitch in NS["PITCHES_MM"]:
            for f in np.arange(.25, 8.01, .25):
                for sigma in [0, .01, .5]:
                    for phase in [0, 45, 90, 360]:
                        m = NS["measurements"](f, sigma, pitch, phase)
                        self.assertTrue(np.all(np.isfinite(m["values"])))
                        self.assertGreaterEqual(m["values"].min(), .05-1e-13)
                        self.assertLessEqual(m["values"].max(), .95+1e-13)
                        self.assertLessEqual(m["alias"], m["nyquist"]+1e-13)
                        if m["fit"] is not None:
                            self.assertAlmostEqual(m["fit"][0], .9*m["pre_mtf"], places=10)


if __name__ == "__main__":
    unittest.main()
