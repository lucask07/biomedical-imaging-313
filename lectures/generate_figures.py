"""Reproducible scientific figures for the first three imaging lectures.

All targets are synthetic. No patient data, downloaded images, or random inputs.
Run with the repository's scientific Python environment.
"""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build" / "lectures"
BUILD.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(BUILD / "matplotlib"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.optimize import brentq

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
BLUE, TEAL, ORANGE, RED = "#173F58", "#157A80", "#A86914", "#B54252"
plt.rcParams.update({"font.size": 18, "axes.titlesize": 18, "axes.labelsize": 18,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "figure.facecolor": "white", "savefig.facecolor": "white",
                     "pdf.fonttype": 42, "axes.titlepad": 12})


def save(fig, name):
    fig.savefig(OUT / (name + ".pdf"), bbox_inches="tight", pad_inches=.08)
    plt.close(fig)


def grid(ax):
    ax.grid(alpha=.18)


def gray(ax, data, extent, title):
    ax.imshow(data, cmap="gray", origin="lower", vmin=0, vmax=1,
              extent=extent, interpolation="nearest")
    ax.set(title=title, xlabel="x (mm)", ylabel="y (mm)")


# 01: a physical forward model for parallel transmission measurements.
n = 600
dx = 10/n
x = (np.arange(n)+.5)*dx
xx, yy = np.meshgrid(x, x)
mu = np.full_like(xx, .02)
for cx, cy, radius, delta_mu in [(4, 3, .8, .12), (4, 7, .8, .12), (7.5, 5, 1.1, .07)]:
    mu += delta_mu*((xx-cx)**2+(yy-cy)**2 <= radius**2)
transmission = np.exp(-mu.sum(axis=0)*dx)
fig, ax = plt.subplots(1, 2, figsize=(12, 4.2), constrained_layout=True)
im = ax[0].imshow(mu, origin="lower", extent=[0,10,0,10], cmap="viridis", vmin=0, vmax=.15)
ax[0].set(title="Synthetic attenuation map", xlabel="x (mm)", ylabel="Depth y (mm)")
fig.colorbar(im, ax=ax[0], label="Attenuation coefficient (mm⁻¹)", shrink=.85)
ax[1].plot(x, transmission, color=BLUE, lw=2)
ax[1].set(title="Transmission along vertical paths", xlabel="Detector position x (mm)",
          ylabel="Transmitted / incident intensity", xlim=(0,10), ylim=(0,1))
grid(ax[1])
save(fig, "01_projection")

# 01: loss of spatial detail under numerical Gaussian convolution.
n, length = 800, 4.
dx = length/n
x = (np.arange(n)+.5)*dx
xx, yy = np.meshgrid(x, x)
target = np.full_like(xx, .1)
target[(xx-.9)**2+(yy-2)**2 < .5**2] = .9
for left, width in [(1.8,.12), (2.07,.12), (2.5,.25), (3.05,.25)]:
    target[(xx>left)&(xx<left+width)&(yy>1)&(yy<3)] = .9
fig, ax = plt.subplots(1, 3, figsize=(12, 4), constrained_layout=True)
for a, sigma in zip(ax, [0,.08,.25]):
    blurred = target if sigma == 0 else gaussian_filter(target, sigma/dx, mode="nearest")
    gray(a, blurred, [0,4,0,4], "Object" if sigma==0 else f"Gaussian blur: σ = {sigma:g} mm")
save(fig, "01_blur")

# 02: sinusoidal objects, phase, and exact component amplitudes.
x = np.linspace(0,4,1600,endpoint=False)
fig, ax = plt.subplots(1,3,figsize=(12,3.6),constrained_layout=True)
for a, f in zip(ax,[.5,1,2]):
    data=np.broadcast_to(.5+.45*np.cos(2*np.pi*f*x),(500,len(x)))
    gray(a,data,[0,4,0,2],f"f = {f:g} cycles/mm")
save(fig,"02_gratings")

fig, a = plt.subplots(figsize=(12,3.6),constrained_layout=True)
for phi,color,label in [(0,BLUE,"Phase 0°"),(np.pi/2,ORANGE,"Phase 90°")]:
    a.plot(x,.5+.45*np.cos(2*np.pi*x+phi),color=color,lw=2,label=label)
a.set(xlabel="Position x (mm)",ylabel="Normalized intensity",xlim=(0,3),ylim=(0,1))
a.legend(loc="upper right",ncol=2)
grid(a)
save(fig,"02_phase")

fig, ax=plt.subplots(1,2,figsize=(12,3.8),constrained_layout=True)
combined=.5+.25*np.cos(2*np.pi*x)+.1*np.cos(2*np.pi*3*x)
ax[0].plot(x,combined,color=BLUE,lw=2)
ax[0].set(title="Mean + 1 cycle/mm + 3 cycles/mm",xlabel="Position x (mm)",ylabel="Normalized intensity",xlim=(0,4),ylim=(0,1))
marker, stems, baseline=ax[1].stem([0,1,3],[.5,.25,.1],basefmt=" ")
plt.setp(marker,color=TEAL,markersize=9)
plt.setp(stems,color=TEAL,linewidth=3)
ax[1].set(title="Mean and cosine amplitudes",xlabel="Spatial frequency (cycles/mm)",ylabel="Amplitude (normalized intensity)",xlim=(-.3,3.5),ylim=(0,.6))
for a in ax:grid(a)
save(fig,"02_components")

# 02: periodic image/spectrum pairs with components exactly on DFT bins.
n,L=256,4.
pos=np.arange(n)*L/n
xx,yy=np.meshgrid(pos,pos)
freq=np.fft.fftshift(np.fft.fftfreq(n,L/n))
df=1/L
fig,ax=plt.subplots(2,3,figsize=(12,5.4),constrained_layout=True)
for col,(u,v,label) in enumerate([(1,0,"Vertical stripes"),(0,1,"Horizontal stripes"),(.75,.75,"Diagonal stripes")]):
    image=.5+.45*np.cos(2*np.pi*(u*xx+v*yy))
    gray(ax[0,col],image,[0,L,0,L],label)
    spectrum=abs(np.fft.fftshift(np.fft.fft2(image)))/(.5*n*n)
    ax[1,col].imshow(spectrum,origin="lower",extent=[freq[0]-df/2,freq[-1]+df/2,freq[0]-df/2,freq[-1]+df/2],cmap="magma",vmin=0,vmax=1,interpolation="nearest")
    ax[1,col].set(xlabel="u (cycles/mm)",ylabel="v (cycles/mm)",xlim=(-2,2),ylim=(-2,2),xticks=[-2,0,2],yticks=[-2,0,2])
    ax[1,col].set_title("Fourier magnitude / DC",fontsize=16,pad=5)
save(fig,"02_orientation")

fig,a=plt.subplots(figsize=(12,3.6),constrained_layout=True)
samples_x=np.arange(0,4.001,.25)
a.plot(x,.5+.4*np.cos(2*np.pi*3*x),color=TEAL,lw=2,label="Object: 3 cycles/mm")
a.plot(x,.5+.4*np.cos(2*np.pi*x),color=ORANGE,lw=2,ls="--",label="Alias: 1 cycle/mm")
a.plot(samples_x,.5+.4*np.cos(2*np.pi*3*samples_x),"o",color=BLUE,label="Samples every 0.25 mm",ms=6)
a.set(xlabel="Position x (mm)",ylabel="Normalized intensity",xlim=(0,4),ylim=(0,1.16))
a.legend(ncol=3,loc="upper center",fontsize=16)
grid(a)
np.testing.assert_allclose(np.cos(2*np.pi*3*samples_x),np.cos(2*np.pi*samples_x),atol=1e-13)
save(fig,"02_alias")

# 03: Gaussian point responses, convolution, and transfer functions.
pos=np.linspace(-1,1,800)
xx,yy=np.meshgrid(pos,pos)
fig,ax=plt.subplots(1,2,figsize=(11,4),constrained_layout=True)
for a,sigma in zip(ax,[.08,.25]):
    gray(a,np.exp(-(xx*xx+yy*yy)/(2*sigma*sigma)),[-1,1,-1,1],f"Gaussian PSF: σ = {sigma:g} mm")
    a.set(xlabel="Offset x (mm)",ylabel="Offset y (mm)")
save(fig,"03_psf_images")

fig,ax=plt.subplots(1,2,figsize=(12,3.8),constrained_layout=True)
x=np.linspace(-1.3,1.3,1600)
for a,sigma in zip(ax,[.08,.25]):
    response=np.zeros_like(x)
    for center in [-.3,.3]:
        component=.5*np.exp(-.5*((x-center)/sigma)**2)/(np.sqrt(2*np.pi)*sigma)
        response+=component
        a.plot(x,component,color=ORANGE,lw=1.4,ls="--")
    a.plot(x,response,color=BLUE,lw=2.5,label="Sum of point responses")
    a.set(title=f"Point separation 0.60 mm; σ = {sigma:g} mm",xlabel="Position x (mm)",ylabel="Line-response density (mm⁻¹)",xlim=(-1.3,1.3),ylim=(0,2.8))
    grid(a)
ax[0].legend(loc="upper right",fontsize=14)
save(fig,"03_two_points")

fig,ax=plt.subplots(1,2,figsize=(12,3.8),constrained_layout=True)
x=np.linspace(-1,1,1600)
f=np.linspace(0,8,1600)
for sigma,color in [(.04,TEAL),(.25,ORANGE)]:
    label=f"σ = {sigma:g} mm"
    ax[0].plot(x,np.exp(-.5*(x/sigma)**2),color=color,lw=2,label=label)
    ax[1].plot(f,np.exp(-2*np.pi**2*sigma*sigma*f*f),color=color,lw=2,label=label)
ax[0].set(title="PSF central profile",xlabel="Offset x (mm)",ylabel="PSF / peak",xlim=(-1,1),ylim=(0,1.08))
ax[1].set(title="Optical MTF",xlabel="Spatial frequency (cycles/mm)",ylabel="Contrast transfer",xlim=(0,8),ylim=(0,1.08))
for a in ax:a.legend();grid(a)
save(fig,"03_psf_mtf")

x=np.linspace(0,3.2,1600)
p=.4
centers=(np.arange(8)+.5)*p
values=.5*(1+.9*np.sinc(p)*np.cos(2*np.pi*centers))
fig,a=plt.subplots(figsize=(12,3.6),constrained_layout=True)
a.plot(x,.5+.45*np.cos(2*np.pi*x),color=TEAL,lw=2,label="Continuous intensity")
a.stairs(values,np.arange(9)*p,color=ORANGE,lw=2,label="Pixel averages",baseline=None)
a.plot(centers,values,"o",color=ORANGE,ms=6,label="Pixel centers")
a.set(xlabel="Position x (mm)",ylabel="Normalized intensity",xlim=(0,3.2),ylim=(0,1.17))
a.legend(ncol=3,loc="upper center",fontsize=16)
grid(a)
save(fig,"03_pixel_average")

f=np.linspace(0,8,1600)
sigma,p=.04,.1
opt=np.exp(-2*np.pi**2*sigma*sigma*f*f)
pixel=abs(np.sinc(p*f))
fig,a=plt.subplots(figsize=(12,3.7),constrained_layout=True)
a.plot(f,opt,color=TEAL,lw=2,label="Optical blur")
a.plot(f,pixel,color=ORANGE,lw=2,label="Pixel averaging")
a.plot(f,opt*pixel,color=BLUE,lw=3,label="Combined before sampling")
a.axvline(1/(2*p),color=RED,ls=":",lw=2,label="Nyquist frequency")
a.axhline(.5,color=".6",ls="--",lw=1)
a.axvspan(1/(2*p),8,color=RED,alpha=.06)
a.set(title="σ = 0.04 mm; pixel spacing p = 0.10 mm",xlabel="Spatial frequency (cycles/mm)",ylabel="MTF",xlim=(0,8),ylim=(0,1.1))
a.legend(loc="upper right",fontsize=16)
grid(a)
save(fig,"03_combined_mtf")


# Additional scientific transform-pair and directional-response figures.
fig, ax = plt.subplots(1,2,figsize=(12,3.1),constrained_layout=True)
a=2.0
ax[0].plot([-3,-a/2,-a/2,a/2,a/2,3],[0,0,1,1,0,0],color=BLUE,lw=2.5)
ax[0].set(title="Unit-height rectangle: a = 2 mm",xlabel="Position x (mm)",ylabel="r(x)",xlim=(-3,3),ylim=(-.12,1.25))
u=np.linspace(-2,2,1601)
ax[1].plot(u,a*np.sinc(a*u),color=TEAL,lw=2.5)
ax[1].axhline(0,color=".5",lw=.8)
ax[1].set(title="Signed, real Fourier transform",xlabel="u (cycles/mm)",ylabel="R(u) (mm)",xlim=(-2,2),ylim=(-.6,2.2))
for ax_i in ax:grid(ax_i)
save(fig,"02_rect_transform")

fig,ax=plt.subplots(1,2,figsize=(12,3.1),constrained_layout=True)
x=np.linspace(-1.5,1.5,1601);u=np.linspace(-4,4,1601)
for sigma,color in [(.2,TEAL),(.4,ORANGE)]:
    ax[0].plot(x,np.exp(-.5*(x/sigma)**2)/(np.sqrt(2*np.pi)*sigma),color=color,lw=2,label=f"σ = {sigma:g} mm")
    ax[1].plot(u,np.exp(-2*np.pi**2*sigma**2*u**2),color=color,lw=2)
ax[0].set(title="Unit-area spatial Gaussians",xlabel="Position x (mm)",ylabel="q(x) (mm⁻¹)",xlim=(-1.5,1.5),ylim=(0,2.2))
ax[1].set(title="Fourier transforms",xlabel="u (cycles/mm)",ylabel="Q(u)",xlim=(-4,4),ylim=(0,1.1))
ax[0].legend(fontsize=14)
for ax_i in ax:grid(ax_i)
save(fig,"02_gaussian_transform")

fig,ax=plt.subplots(1,2,figsize=(12,3.4),constrained_layout=True)
a,b=.6,.3
pos=np.linspace(-1,1,600);xx,yy=np.meshgrid(pos,pos)
ax[0].imshow(np.exp(-np.pi*((xx/a)**2+(yy/b)**2)),origin="lower",extent=[-1,1,-1,1],cmap="gray",vmin=0,vmax=1)
ax[0].set(title="PSF / peak: a = 0.60, b = 0.30 mm",xlabel="Offset x (mm)",ylabel="Offset y (mm)")
u=np.linspace(0,5,1601)
ax[1].plot(u,np.exp(-np.pi*(a*u)**2),lw=2,color=TEAL,label="Along u: H(u, 0)")
ax[1].plot(u,np.exp(-np.pi*(b*u)**2),lw=2,color=ORANGE,label="Along v: H(0, v)")
ax[1].set(title="Unit-DC transfer function",xlabel="Spatial frequency (cycles/mm)",ylabel="H along each frequency axis",xlim=(0,5),ylim=(0,1.08))
ax[1].legend(fontsize=14)
grid(ax[1])
save(fig,"03_directional_response")

# Store independent numeric checks outside the student deliverables.
metrics={}
for sigma in [.04,.25]:
    response=lambda f:np.exp(-2*np.pi**2*sigma*sigma*f*f)*np.sinc(.1*f)
    metrics[str(sigma)]={"fwhm_mm":float(2*np.sqrt(2*np.log(2))*sigma),
                         "mtf_at_1":float(response(1)),
                         "contrast_at_1":float(.9*response(1)),
                         "mtf50_cycles_per_mm":float(brentq(lambda f:response(f)-.5,0,10))}
assert metrics["0.04"]["mtf_at_1"] > metrics["0.25"]["mtf_at_1"]
(BUILD/"checked_metrics.json").write_text(json.dumps(metrics,indent=2)+"\n")
print(f"Generated {len(list(OUT.glob('*.pdf')))} scientific figures")
print(json.dumps(metrics,indent=2))
