===============================================================
README  —  Gravity Is Time
===============================================================

Author ........:  Edrick Francis G. Herrera
Last edited ...:  May 30, 2025
LaTeX engine ..:  pdfLaTeX
Bib manager ...:  biblatex + biber
===============================================================

ABSTRACT:
We show that a single scalar clock field τ(x) can account for all
gravitational phenomena traditionally attributed to curved spacetime
and cold dark matter.  The minimal model collapses gravity to one
degree of freedom, passes Solar-System tests, fits super-nova
luminosity distances without a cosmological constant, and reproduces
Bullet-Cluster lensing via collision-less τ-halos.  Upcoming optical
clock networks, weak-lensing surveys, and LIGO-Virgo-KAGRA Run O5 will
provide decisive falsification at the 1 % level.

1.  OVERVIEW
----------------------------------------------------------------
This repository contains the complete source for the thesis
“Scalar-Time Gravity and Cosmic Red-Shift.”  It includes:

  • main.tex ............ master driver that inputs chapters,
                          appendices, and the bibliography
  • Chapters_#.tex....... numbered chapter files
  • Appendices_#.tex .... A–F, each in its own .tex
  • figures/ ............ TikZ figure .tex files and external
                          images (PNG/PDF) called by \includegraphics
  • code/ ............... Python scripts that reproduce every
                          figure (Appendix F)
  • references.bib .......single BibLaTeX database

Appendices B–F are wrapped in `refsection` environments so each prints
its own bibliography subset, yet all citations come from one
`references.bib` file.


2.  DIRECTORY TREE
----------------------------------------------------------------
.
├─ main.tex
├─ references.bib
├─ Abstract.tex
├─ Chapter1.tex
├─ Chapter1.tex
├─ Chapter1.tex
├─ Chapter2.tex 
├─ Chapter3.tex
├─ Chapter4.tex
├─ Chapter5.tex
├─ Chapter6.tex
├─ Conclusion.tex
├─ Glossary.tex
├─ Appendix_A.tex
├─ Appendix_B.tex
├─ Appendix_C.tex
├─ Appendix_D.tex
├─ Appendix_E.tex
├─ Appendix_F.tex
│ 
├─ figs/
│   ├─ fig01_clock_gradient.tex
│   ├─ fig02_grav_redshift.tex
│   ├─ fig03_dist_modulus.tex
│   ├─ fig04_background_Ez.tex
│   ├─ fig05_omega_cross.tex
│   ├─ fig06_bao_residuals.tex
│   ├─ fig07_bao_cmb.tex
│   ├─ fig08_redshift_drift.tex
│   ├─ fig09_Ez_curve.tex
│   ├─ fig10_weak_lensing.tex
│   └─ fig12_C5_Wave_Packet.tex
│   
├─ images/
│   ├─ fig11_Twobody_Cluster.png
└─ code/
   ├─ fig01_clock_gradient.py
   ├─ fig02_grav_redshift.py
   ├─ fig03_dist_modulus.py
   ├─ fig04_background_Ez.py
   ├─ fig05_omega_cross.py
   ├─ fig06_bao_residuals.py
   ├─ fig07_bao_cmb.py
   ├─ fig08_redshift_drift.py
   ├─ fig09_Ez_curve.py
   ├─ fig10_weak_lensing.py
   ├─ fig11_Twobody_Cluster.py
   └─ Wave_Packet.py


6.  CONTACT
----------------------------------------------------------------
Edrick Francis G. Herrera — codeherrera333@gmail.com

If you spot an error or have questions, please open an issue at
https://github.com/CodeFrancis333/GravityIsTime.git or email directly.
