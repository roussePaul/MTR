\documentclass{article}
\usepackage{amsfonts, amsmath, amsthm, amssymb,latexsym}
\usepackage{stmaryrd}

\usepackage{subcaption}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows, positioning, calc, fit, arrows, decorations.pathreplacing}
\usepackage{pgfplots}
\usepackage{siunitx}

\usepackage{enumitem}

\begin{document}

\title{State space discretization}
\maketitle

\section{Investigation over discretization of the state space}
What are the constraints that does exists on the discretization of the state space?
Many parts of my maser thesis will be justified by this.
Therefore I need to have a clear approach about it.

This part will justify all the other parts about the different models that I used.
Try to be as theoretical as possible.
 


In this section we will try to understand what are the constraints that apply on the discretization of the state space.
Our main goal i to verify an LTL formula over the state space. For a given discrete model of the robot, we will say that the discretization of the state space is valid if we are able to find a controller that verify the formula.
The main problem about the discretization is that it will depend on the LTL formula that we would like to verify. For example if we need to verify the formula $\Diamond \square a$, then the region $a$ must be discretized enough in order that it exist a controller (a finite state controller) that make this region attractive.
Here I am questioning the feasibility of the LTL formula in the discretization.

In the following paragraph we will try to see what are the impact of it for a monotone linear model and a regular uniform.
This part just aim to give some inside about the discretization problem:
We will start

Constraints on the state space discretization:
\begin{itemize}[noitemsep,topsep=0pt,parsep=0pt,partopsep=0pt]
\item the goals regions needs to be reachable and eventual
\item size of $V_\mathbf{w}$
\end{itemize}

\end{document}
