
README  —  Gravity Is Time
===============================================================

Author :  E. F. G. Herrera <br>
Last edited :  May 30, 2025 <br>
LaTeX engine :  pdfLaTeX <br>
Bib manager :  biblatex + biber <br>


ABSTRACT:<br>
===============================================================
We show that a single scalar clock field τ(x) can account for all
gravitational phenomena traditionally attributed to curved spacetime
and cold dark matter.  The minimal model collapses gravity to one
degree of freedom, passes Solar-System tests, fits super-nova
luminosity distances without a cosmological constant, and reproduces
Bullet-Cluster lensing via collision-less τ-halos.  Upcoming optical
clock networks, weak-lensing surveys, and LIGO-Virgo-KAGRA Run O5 will
provide decisive falsification at the 1 % level. 
<br>

1.  OVERVIEW
----------------------------------------------------------------
This repository contains the complete source for the thesis
“Scalar-Time Gravity and Cosmic Red-Shift.”  It includes: <br>

  • main.tex .................  master driver that inputs chapters,
                          appendices, and the bibliography <br>
  • Chapters_#.tex....... numbered chapter files <br>
  • Appendices_#.tex .... A–F, each in its own .tex <br>
  • figures/ ............ TikZ figure .tex files and external
                          images (PNG/PDF) called by \includegraphics<br>
  • code/ ............... Python scripts that reproduce every
                          figure (Appendix F) <br>
  • references.bib .......single BibLaTeX database <br>

Appendices B–F are wrapped in `refsection` environments so each prints
its own bibliography subset, yet all citations come from one
`references.bib` file.<br>


2.  DIRECTORY TREE
----------------------------------------------------------------
├─ main.tex <br>
├─ references.bib <br>
├─ Abstract.tex <br>
├─ Chapter1.tex <br>
├─ Chapter1.tex <br>
├─ Chapter1.tex <br>
├─ Chapter2.tex <br>
├─ Chapter3.tex <br>
├─ Chapter4.tex <br>
├─ Chapter5.tex <br>
├─ Chapter6.tex <br>
├─ Conclusion.tex  <br>
├─ Glossary.tex<br>
├─ Appendix_A.tex<br>
├─ Appendix_B.tex<br>
├─ Appendix_C.tex<br>
├─ Appendix_D.tex<br>
├─ Appendix_E.tex<br>
├─ Appendix_F.tex<br>
│ <br>
├─ figs/<br>
│   ├─ fig01_clock_gradient.tex<br>
│   ├─ fig02_grav_redshift.tex<br>
│   ├─ fig03_dist_modulus.tex<br>
│   ├─ fig04_background_Ez.tex<br>
│   ├─ fig05_omega_cross.tex<br>
│   ├─ fig06_bao_residuals.tex<br>
│   ├─ fig07_bao_cmb.tex<br>
│   ├─ fig08_redshift_drift.tex<br>
│   ├─ fig09_Ez_curve.tex<br>
│   ├─ fig10_weak_lensing.tex<br>
│   └─ fig12_C5_Wave_Packet.tex<br>
│   <br>
├─ images/<br>
│   ├─ fig11_Twobody_Cluster.png<br>
└─ code/<br>
   ├─ fig01_clock_gradient.py<br>
   ├─ fig02_grav_redshift.py<br>
   ├─ fig03_dist_modulus.py<br>
   ├─ fig04_background_Ez.py<br>
   ├─ fig05_omega_cross.py<br>
   ├─ fig06_bao_residuals.py<br>
   ├─ fig07_bao_cmb.py<br>
   ├─ fig08_redshift_drift.py<br>
   ├─ fig09_Ez_curve.py<br>
   ├─ fig10_weak_lensing.py<br>
   ├─ fig11_Twobody_Cluster.py<br>
   └─ Wave_Packet.py<br>
<br>

6.  CONTACT
----------------------------------------------------------------
Edrick Francis G. Herrera — codeherrera333@gmail.com

If you spot an error or have questions, please open an issue at
https://github.com/CodeFrancis333/GravityIsTime.git or email directly.

Also if you wanted to be part of this paper, I'm looking for help for the full Boltzmann Run (CMB peaks)
using: Cosmic Linear Anisotropy Solving System (https://github.com/lesgourg/class_public.git)
