Simulation chapter

This part is mainly based on controllability issues.
I need to talk before about the self loops because this create one constraint on the state space discretization
I need to talk about over lapping before as well because it explains the fact that the 1 input reduced model is better than the second int model for L small
I must begin with the different constraints on the state space discretization for each of the model
Then after all this I talk about when to choose each of the model according to the size of the environment

* Introduction
	- say what I am going to talk about what I want to achieve in this chapter
	- why do I choose to focus on the single integrator
	- discretization of the environment notations

Organized in 2 parts

/////////////////////////////////////////
// First part // Algorithm Justification:

introduction about the single integrator  used in order to justify it

*** Self loops ***
	!! pb pas vraiment à propos de la réduction, plus à propos de l'algo
	- arguments about considering the self loops (this is about the strategy chosen for the algorithm, not about the abstraction)
		. special case where there is no inputs: single integrator
			¤ why do I choose the single integrator?
			-> I have to choose a model, this case is interesting to show that it is really efficient in some case
		. give the link between state space discretization and sampling rate
		. way smaller discretization for the same sampling rate
		%% show the graphs about the single integrator

	- disadvantage of self loops
		-> create asynchronous systems that are terrible for multi agent systems, we are loosing time information which is super bad for synchronisation of course
		can I find a number to talk about it

*** Size of the fixed point ***
	%% plot the influence of the size of the fixed point for the single integrator
	- show that the best option is to limit it as possible (but it does worth it for small number of fixed points)

//////////////////////////////
// Second part // Abstraction: 

*** Self loops ***
	- the reduction tend to suppress self loops in transient transitions:
		. ie in order to have self loops, you need to have U(n) = U(n-1)
		. suppress all the transients that last not so long
		. in another scenario, the only way to suppress self loops in transiant states is to increase the state discretization
		%% example of the second integrator that needs 2 steps to go backward
		%% plot the case of the reduced model that have overlapps
		%% show the second int model discretization that we need for it.

		. overlapps:
			¤ show a graph of what is happening in the velocity between the dbl and dbl1r
			¤ say that it force us to increase the number of cells in the second case to see what is happening

*** Size of the state space / FTS ***
	In 2 parts: study of the number of nodes, then of the number of edges

	- memories are really bad (not so sure) for the state space representation (they you need to consider all the past events) 
		. compare the size of the state space for the original model and the previous one
		. fixed points number depends on the state size
		-> just underline the fact that the size of a set of nodes in a rectangle have also the set of all the inputs and as the algorithm is based on it
		then the complexity is growing fastly
		. give a formula on the number of nodes, it will be much better for understanding it
		. compare it to any models

	- study when it worth it to add memories or when it will just increase the size of the state space
		. explain when it worth to use reachable sets from invariants or from observation -> link it to the model
		%% make 2 curves about it: one will be the reachable set from the invariant, the other will be from the observation
		. show that the one with the invariant is always more over approximated than the one with the observation
		. there is a link between this and the noise (basically we can model more noise because there is some more space between the lyapunov function and the other estimation)

*** State space discretization and sampling rate constraints for feasability ***
	- explain that there is no rules about it, it is specific to applications

	~ slowly converge to the idea that for a model it might not exist any parameter set solution for the problem
	~ abstraction is then not precise enough
	- constraint on the discretization for all the models
		%% global constraints
			upper constraint: not going out of the environment
		%% specific constraints
			no self loops on the velocity in the 2sd int model
			no going backward for the simple int
		%% show that for some models, it is not possible to find abstraction controllable for all the sampling rates
			too noisy
	
	- conclude with a link between the size of the environment and the feasability
	

*** Feasability (abstr) ***
	- be clear in the introduction:
		. we use CPU time computation just to show that the complexity of the abstraction is growing up to a point where there is no solution
		  but this part intend to show when the abstraction is good at finding a solution

	%% curve about the smallest env size models for each of them
		. explain why dbl1 is smaller (overlapp)
		. explain why there is a minimal length for feasability for each of the models
		. mention why this curve is important (usefull to choose the models)

*** Noise *** (abstr)
	%% presentation of what apply to our model:
		. give the values of the constraints on the noise for dbl1 for a chosen sampling rate, introduce this with a curve of an admissible noise sequence
		. admissible noise set not bigger for a constant input: show a corve of the maximum noise set
	
	%% influence of the number of inputs:
		. plot some curves for 1, 2 or 3 inputs memories
	
	%% can I link it to the sampling rate (ie plot the bode diagrams according to the sampling rates)
		. plot the maximum oscillation or the max peak for the noise according to the sampling rate
		. link between this and the computation of the invariants
		. acceptable error is higher at the beginning the same on infinite time
	
* Conclusion
	- their is a power 10 of difference between the min size for the reduced model and the not reduced model


TODO:
	I need to redo the graph on the controllability so that it match my experiments
	Keep studying what is happening on the noise
