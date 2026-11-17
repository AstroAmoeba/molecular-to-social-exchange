# Kinetic exchange models: From molecular physics to social science

**Marco Patriarca**\*  
National Institute of Chemical Physics and Biophysics, Răvala 10, Tallinn 15042, Estonia

**Anirban Chakraborti**†  
Laboratoire de Mathématiques Appliquées aux Systèmes, École Centrale Paris, 92290 Châtenay-Malabry, France

(Dated: November 27, 2024)

---

## ABSTRACT

We discuss several multi-agent models that have their origin in the kinetic exchange theory of statistical mechanics and have been recently applied to a variety of problems in the social sciences. This class of models can be easily adapted for simulations in areas other than physics, such as the modeling of income and wealth distributions in economics and opinion dynamics in sociology.

---

## I. INTRODUCTION

The application of probability theory to the study of gases led to the formulation of the kinetic theory of gases, prepared the basis for the formulation of the Maxwell velocity distribution, and later, for the development of statistical mechanics.¹⁻³ The initial triumph was that the empirical laws of thermodynamics were obtained from the basic assumptions of statistical mechanics. Today we understand that the scope of statistical mechanics is much broader. Because it has the tools to treat macroscopic systems with a large number of microscopic constituents, it can be naturally applied to many types of systems.

Kinetic exchange models, the subject of this article, are stochastic models which have a straightforward interpretation in terms of energy exchanges in a gas. However, they can be suitably adapted and used to study problems in the social sciences, as illustrated by recent work.⁴⁻⁷ The applications of kinetic exchange models to problems in fields from molecular physics to the social sciences illustrates the historical link between statistical mechanics and the social sciences. Recently, this link has been rediscovered due to the development of complex systems theory and social dynamics. In fact, statistics, which was an important basis for Maxwell's and Boltzmann's work and the foundation of statistical mechanics, originated from the study of demographic data.⁸ The idea that a large number of molecules and a large social group have many important common features, in particular, that they are predictable due to the high number of their components despite their intrinsic random character, was shared by many investigators. Boltzmann wrote that "molecules are like so many individuals, having the most various states of motion," when writing about the foundations of statistical mechanics.⁸,⁹

Multi-agent models are a class of models where the actions and interactions of autonomous agents, which may represent individuals, organizations, societies, etc., can be used to understand the behavior of the system as a whole. The simple formulation and numerical implementation of kinetic exchange models make them attractive in many disciplines. They can be regarded as minimal prototypical models of complex systems consisting of a set of (possibly) heterogeneous units interacting according to simple laws, yet they are able to exhibit well defined states with robust probability distributions.

In this article we focus on the formulation, interpretation, and simulation of a few representative examples of kinetic exchange models. Other social science applications of kinetic exchange models are also summarized.

---

## II. HOMOGENEOUS KINETIC EXCHANGE MODELS

### A. Kinetic exchange models in molecular physics: Thermal relaxation in *d*-dimensions

We introduce the general structure of a kinetic exchange model by a simple example. It is assumed that the *N* (minimally) interacting units {*i*}, with *i* = 1, 2, ..., *N*, are molecules of a gas with no interaction energy and the variables {*w*ᵢ} represent their kinetic energies, such that *w*ᵢ ≥ 0. The time evolution of the system proceeds by a discrete stochastic dynamics. A series of updates of the kinetic energies *w*ᵢ(*t*) are made at the discrete times *t* = 0, 1, ... . Each update takes into account the effect of a collision between two molecules. The time step, which can be set to Δ*t* = 1 without loss of generality, represents the average time interval between two consecutive molecular collisions; that is, on average, after each time step Δ*t*, two molecules *i* and *j* undergo a scattering process and an update of their kinetic energies *w*ᵢ and *w*ⱼ is made.

The evolution of the system is accomplished by the following steps at each time *t*.

1. Randomly choose a pair of molecules *i* and *j* (*i* ≠ *j* and 1 ≤ *i*, *j* ≤ *N*), with kinetic energies *w*ᵢ and *w*ⱼ, respectively; they represent the molecules undergoing a collision.

2. Compute the net amount Δ*w*ᵢⱼ of kinetic energy to be exchanged between the molecules; its value is a function of the initial kinetic energies *w*ᵢ and *w*ⱼ and depends on the model considered.

3. Perform the energy exchange between *i* and *j* by updating their kinetic energies,

$$w_i \rightarrow w_i - \Delta w_{ij} \quad (1a)$$

$$w_j \rightarrow w_j + \Delta w_{ij}. \quad (1b)$$

The total kinetic energy is conserved during an interaction.

4. Set *t* → *t*+1 and go to step 1.

The form of the function Δ*w*ᵢⱼ defines the specific model. Kinetic exchange models describe the dynamics at a microscopic level, based on single molecular collisions. Such a representation can be optimal in terms of simplicity and computational efficiency when the focus is on the energy dynamics, because particles are described by their energy degree of freedom *w* only, rather than by the entire set of their 2*d* position and momentum coordinates, for a *d*-dimensional system.

As our first simple example, consider the reshuffling rule: *w*ᵢ → ε(*w*ᵢ + *w*ⱼ), *w*ⱼ → (1−ε)(*w*ᵢ + *w*ⱼ), where ε is a stochastic variable drawn as a uniform random number between 0 and 1. This rule corresponds to Δ*w*ᵢⱼ = (1−ε)*w*ᵢ − ε*w*ⱼ. In this case, the algorithm we have outlined leads from arbitrary initial conditions to the Boltzmann-Gibbs energy distribution at equilibrium, *f*(*w*) = β exp(−β*w*), where β = 1/⟨*w*⟩ and ⟨*w*⟩ represents the mean energy of a single molecule. The theoretical derivations of this result using the Boltzmann transport equation, or entropy maximization principle, or simple probabilistic arguments, can be found in most standard textbooks of statistical mechanics.

As a more general example, consider the relaxation in energy space of a gas in *d*-dimensions. We assume that *d* > 1 because the momentum and energy distributions of a one-dimensional gas (where only head-on collisions occur) do not change with time. Although the model can be conceived most easily for a gas in three dimensions, the most surprising features of kinetic exchange models appear for a gas in an arbitrary number of dimensions, a case relevant for the treatment of heterogeneous systems in Sec. III. For a gas in *d*-dimensions the form of the update rule, and in particular of Δ*w*ᵢⱼ, can be derived exactly from energy and momentum conservation during a collision between two particles *i* and *j*. If the respective *d*-dimensional vectors of the particle initial momenta are **p**ᵢ and **p**ⱼ, we find¹⁰

$$\Delta w_{ij} = r_i w_i - r_j w_j \quad (2)$$

$$r_k = \cos^2 \alpha_k \quad (k = i, j) \quad (3)$$

$$\cos \alpha_k = \frac{\mathbf{p}_k \cdot \Delta \mathbf{p}_{ij}}{|\mathbf{p}_k| |\Delta \mathbf{p}_{ij}|}, \quad (4)$$

where cos αₖ is the direction cosine of momentum **p**ₖ (*k* = *i*, *j*) with respect to the direction of the transferred momentum Δ**p**ᵢⱼ = **p**ᵢ − **p**ⱼ. The directions of the two colliding particles can be assumed to be random using the hypothesis of molecular chaos.³

We can now study the time evolution by randomly choosing at each time step two new values for *r*ₖ in Eq. (2), instead of maintaining a list of momentum coordinates, as is commonly done in a molecular dynamics simulation. Then we use Eq. (1) to compute the new particle energies *w*ᵢ and *w*ⱼ. Note that the *r*ₖ's are not uniformly distributed in (0, 1), and thus the form of their probability distribution function has to be chosen with some prudence. In fact, their distribution strongly depends on the spatial dimension *d*, their average value being ⟨*r*ₖ⟩ = 1/*d*; see Ref. 10 for further details. This dependence of ⟨*r*ₖ⟩ on *d* can be intuitively understood from kinetic theory: the greater the value of *d*, the more unlikely it becomes that *r*ₖ assumes values close to *r*ₖ = 1 (corresponding to a one-dimensional-like head on collision). Hence, a simple and computationally efficient choice is a uniform random distribution *f*(*r*ₖ), limited in the interval (0, 2/*d*), such that the average value ⟨*r*ₖ⟩ = 1/*d*.

Simulations of this model system using random numbers in place of the *r*ᵢ's in Eq. (2), for *d* = 2, give the equilibrium Boltzmann-Gibbs distribution: *f*(*w*) = β exp(−β*w*), where β = 1/⟨*w*⟩, as before. For *d* > 2, we obtain the *d*-dimensional generalization of the standard Boltzmann distribution,¹⁰⁻¹² namely the Gamma (Γ) distribution¹³,¹⁴ characterized by a shape parameter α equal to half of the spatial dimension,

$$f(w, \alpha, \theta) = \frac{w^{\alpha-1} e^{-w/\theta}}{\theta^{\alpha} \Gamma(\alpha)} \quad (5)$$

$$\alpha = d/2 \quad (6)$$

$$\theta = \langle w \rangle / \alpha. \quad (7)$$

The scale parameter θ of the Γ-distribution is fixed, by definition, by Eq. (7).¹³,¹⁴ From the equipartition theorem in classical statistical mechanics, *w* = *d k*_B *T*/2. Hence, we see that Eq. (7) identifies the scale parameter θ as the absolute temperature (in energy units) given by θ ≡ *k*_B *T* = 1/β. Therefore, the same Boltzmann factor, exp(−*w*/θ), is present in the equilibrium distribution independently of the dimension *d*, and the prefactor *w*^{α−1} depends on *d*, because it takes into account the phase-space volume proportional to *p*^d ∝ *w*^{d/2}, where *p* is the momentum modulus.

### B. Modeling the wealth distribution

Besides their interpretation in the context of physics, kinetic exchange models are applicable to problems in the social sciences such as opinion dynamics and the modeling of economic systems. The latter models demonstrate their adaptability and promise, particularly in their application to wealth distributions. In this section we consider how some kinetic exchange models describe the formation of the wealth distribution observed in a society, as a consequence of binary wealth exchanges between individuals. We assume here that the standard definition of wealth is the set of all those things with some monetary or exchange value. The shape of a typical wealth distribution is complex, with a Boltzmann-Gibbs (exponential) behavior at lower and intermediate values of wealth, *w* < *w*_c, and a power law (Pareto) tail at the larger wealth values, *w* ≥ *w*_c, where *w*_c is a crossover value that depends on the numerical fitting of the data. The Pareto law is expressed as:

$$f(w) \sim w^{-\alpha-1} \quad (w \ge w_c), \quad (8)$$

where *f*(*w*) is the probability density, and the exponent α is the Pareto exponent, which has a value between 1 and 3. Reference 16 gives concise accounts of empirical, numerical and analytical studies on this subject. Figure 1 shows a plot of the cumulative probability distribution for wealth data. It is more practical to plot the cumulative probability distribution *C*(*w*) = ∫_w^∞ *f*(*w*′) *dw*′ as a function of the wealth *w*, rather than *f*(*w*), because statistical data is usually reported at non-uniform intervals of *w*. Interestingly, when *f*(*w*) is an exponential or a power-law function, then the respective *C*(*w*) is also an exponential or a power-law function. For more details of kinetic wealth exchange models, see Refs. 4, 5, and 7.

**FIG. 1.** Cumulative probability distribution of the net wealth, composed of assets (including cash, stocks, property, and household goods) and liabilities (including mortgages and other debts) in the United Kingdom shown on log-log (main panel) and log-linear (inset) scales. Points represent the data from the Inland Revenue, and solid lines are fits to the Boltzmann-Gibbs (exponential) and Pareto (power) distributions.¹⁵

Among the first examples of kinetic exchange models of markets proposed by non-physicists, we mention the work of Angle, a sociologist.¹⁷⁻²⁰ In the first version of the model¹⁷,¹⁸ the wealth exchanged at a encounter between two agents has the form of Eq. (2), where *r*ᵢ = εκη and *r*ⱼ = (1 − ε)κη. Here κ represents the maximum fraction of wealth that can be lost, ε is a uniform random number in (0, 1), and η is a stochastic variable with the values 0 or 1 with a probability distribution depending on the difference between the wealth of the two agents *w*ᵢ − *w*ⱼ. In the second model by Angle, referred to as the one-parameter inequality process,¹⁹,²⁰ *r*ᵢ = κη and *r*ⱼ = κ(1 − η), with a similar meaning for κ and η. In contrast, in the basic version of the models²¹⁻²³ introduced earlier by the economist, Bennati, Δ*w*ᵢⱼ is a constant, independent of other parameters.

Independent of the above modeling efforts by social scientists, physicists also had made several studies. The first kind of models both with multiplicative and additive exchanges, were proposed by Ispolatov, Krapivski, and Redner.²⁴ In the kinetic exchange models introduced later, we first consider the work of Dragulescu and Yakovenko,²⁵ where *r*ᵢ = 1 − *r*ⱼ = ε, corresponding to a random reshuffling scheme of the total wealth of the two agents. We next consider a simple prototypical kinetic exchange model with a Γ-function equilibrium distribution, which was introduced by Chakraborti and Chakrabarti²⁶ to describe the trade activity between *N* entities (for example, agents, firms, and companies) employing a saving criterion when carrying out their trades. Trades are represented by pair-wise wealth exchanges with the dynamics given by Eq. (1) with

$$\Delta w_{ij} = \kappa(\bar{\epsilon} w_i - \epsilon w_j) = (1 - \lambda)(\bar{\epsilon} w_i - \epsilon w_j), \quad (9)$$

where ε̄ = 1 − ε. The exchange parameter κ ∈ (0, 1) (or the saving parameter λ = 1 − κ) defines the maximum fraction of the wealth *w* in the exchange process (or the minimum fraction of *w* preserved during the exchange). The parameter κ (or λ) also determines the time scale of the relaxation process as well as the mean value ⟨*w*⟩ in equilibrium.²⁷ The equilibrium wealth distribution of the system is well described by the Γ-distribution in Eq. (5), where a fit suggests the empirical formula

$$\alpha = \frac{1 + 2\lambda}{1 - \lambda} = \frac{3}{\kappa} - 2, \quad (10)$$

which relates the shape parameter α to the saving parameter λ. Note that for λ → 0 (or κ → 1), α → 1, corresponding to the exponential function. In all the various models we have mentioned, the equilibrium distribution is well fitted by a Γ-distribution. This shape of the equilibrium distribution shows good agreement with empirical wealth distributions at small and intermediate values¹⁵,²⁸ (see Fig. 1).

Numerical results of the model defined by Eq. (9) are compared in Fig. 2 with a fit based on the Γ-distribution. They were obtained using 10⁴ agents and 10⁴ time steps. The convergence to equilibrium is fast and such a long simulation time was used only to accumulate statistics (every 100 time steps). Note that here one time step is actually a loop over *N* exchanges. The number of agents employed has to be chosen sufficiently large to ensure enough statistics — implying a good quality of the wealth histogram — at the desired frequency scale, otherwise a very irregular histogram may appear at the smallest and largest values of *w*. The value *N* = 10⁵ is still manageable computationally, yet sufficiently large to clearly see frequencies as small as 10⁻⁵.

**FIG. 2.** (Color online) Equilibrium wealth distributions of the model introduced in Ref. 26 and defined by Eq. (9) for different values of the saving parameter λ for linear (top) and semi-log (bottom) scales.

### C. Other social science applications

Lallouache et al.⁶ constructed a homogeneous model for the collective dynamics of opinion formation in a society by modifying the kinetic exchange dynamics studied in the context of markets. In this model the opinion of the *i*th agent is represented by a continuous variable *w*ᵢ ∈ (−1, +1). Interactions between agents who modify their opinions are assumed to take place through random two-body encounters, with a dynamics defined by

$$w_i \rightarrow \lambda[w_i + \epsilon w_j] \quad (11a)$$

$$w_j \rightarrow \lambda[w_j + \epsilon' w_i], \quad (11b)$$

where λ ∈ (0, 1) is the (constant) "conviction" parameter and ε, ε′ ∈ (0, 1) are uncorrelated uniformly distributed stochastic processes. Note that there is no step-wise conservation of opinion, unlike for the preceding wealth models. Remarkably, it is found that there is an appearance of polarity or consensus, starting from initial random disorder (where the *w*ᵢ are uniformly distributed with positive and negative values). In the language of physics, there is a "spontaneous symmetry-breaking transition" in the system: starting from the mean value of *w*ᵢ, *w̄*(0) = 0, the system evolves either to the "para" state with *w̄*(*t* > τ) = 0, where all agents have the opinion zero (for values of λ ≤ 2/3), or to the "symmetry broken" state, with *w̄*(*t* > τ) ≠ 0, where all the agents have either all positive or all negative opinions (for λ ≥ 2/3). The time *t* > τ, where τ is the relaxation time for the system. The relaxation behavior of the system shows a critical divergence of τ at λ = λ_c = 2/3. Sen²⁹ generalized the model by Lallouache et al. by introducing an additional parameter μ to represent the influencing ability of individuals and studied the corresponding phase transitions.

In a different context, similar in spirit to the work presented in Refs. 30 and 31, Ghosh et al.³² considered an economic model in which there is a poverty threshold θ > 0 such that at any time *t*, at least one of the two interacting agents is "poor;" that is, its wealth satisfies *w* < θ. The central role assigned to the poor traders produces various new features such as a different form of the equilibrium distribution and a phase transition in the fraction of poor agents as a function of θ. These models of kinetic exchanges, which draw inspiration from various socio-economic contexts, may also serve the purpose of introducing the ideas of phase transitions and critical phenomena in statistical physics.

---

## III. HETEROGENEOUS KINETIC EXCHANGE MODELS

An interesting generalization of the homogeneous kinetic exchange models we have discussed so far is the introduction of heterogeneity. Probably the most relevant applications of heterogeneous kinetic exchange models in the social sciences is the prediction of a realistic shape for the wealth distribution which includes the Pareto power law at the largest wealth values (see Fig. 1 and Sec. II B).

We consider again the model defined by Eq. (9) and introduce heterogeneity by diversifying the parameter κ or equivalently the saving parameter λ, meaning that each term κ*w*ᵢ (or λ*w*ᵢ) is replaced by κᵢ*w*ᵢ (or λᵢ*w*ᵢ), thus obtaining³³

$$\Delta w_{ij} = \bar{\epsilon} \kappa_i w_i - \epsilon \kappa_j w_j = \bar{\epsilon}(1 - \lambda_i) w_i - \epsilon(1 - \lambda_j) w_j. \quad (12)$$

As a simple example, we consider a set of heterogeneous agents with parameters κᵢ uniformly distributed in the interval (0, 1). By repeating the simulations using Eq. (12), it is found that the shape of the separate equilibrium wealth distributions *f*ᵢ(*w*) of each agent is still a Γ-distribution. However, there is a surprise in the wealth distribution of the system *f*(*w*), given by the sum of the wealth distributions of the single agents, *f*(*w*) = Σᵢ *f*ᵢ(*w*). As other analytical and numerical studies have also shown, *f*(*w*) has an exponential form until intermediate *w*-values, and a Pareto power law develops at the largest values of *w* (see Fig. 3).³⁴,³⁵ Such a shape is similar to real wealth distributions such as that shown in Fig. 1. This shape of the equilibrium wealth distribution *f*(*w*) is robust with respect to the details of the system and the values of the other parameters, as long as the values of the κᵢ are sufficiently spread over the entire interval κ = (0, 1). It is the group of agents with κ ≈ 0 (λ ≈ 1) that are crucial for the appearance of a power law. Not all agents have to differ from each other, as is best illustrated by repeating the simulation using a different distribution for the κ-parameters or the λs, in which 99% of the agent population has λ = 0.2, and only 1% of the population is heterogeneous with λ in the interval (0, 1) (see Fig. 4).

The heterogeneous model necessarily uses a finite upper cutoff λ_max < 1, when considering the saving parameter distribution, which directly determines the cutoff *w*_max of the wealth distribution, analogous to the cutoff observed in real distributions: the closer λ_max is to one, the larger *w*_max and the wider the interval in which the power law is observed.³⁶

The λ-cutoff is closely related to the relaxation process, whose time scales for agent *i* is proportional to 1/(1 − λᵢ).²⁷ Thus the slowest convergence rate is determined by 1 − λ_max. The finite λ-cutoff used in simulations of heterogeneous kinetic exchange models is not a limitation of the model, but reflects an important feature of real wealth distributions.

**FIG. 3.** (Color online) Wealth distribution *f*(*w*) for uniformly distributed κᵢ (or λᵢ) in the interval (0, 1); *f*(*w*) is decomposed into partial distributions *f*ᵢ(*w*), where each *f*ᵢ(*w*) is obtained by counting the statistics of those agents with parameter λᵢ in a specific sub-interval (from Ref. 36). (a) Decomposition of *f*(*w*) into ten partial distributions in the λ-subintervals (0, 0.1), (0.1, 0.2) ... (0.9, 1). (b) The last distribution of (a) in the λ-interval (0.9, 1) is decomposed into partial distributions obtained by counting the statistics of agents with λ-subintervals (0.9, 0.91), (0.91, 0.92) ... (0.99, 1). Note how the power law appears as a consequence of the superposition of the partial distributions.

---

## IV. COMMENTS

There are several analytical studies which complement the simulations and empirical studies. We refer the reader to Ref. 16, which gives concise accounts of studies on this subject, along with an exhaustive list of references.

The dynamics of kinetic exchange models are sometimes criticized for being based on an approach that is far from an actual economics perspective. However, such a dynamics can also be derived from microeconomics theory.³⁷ Although standard economics theory assumes that the activities of individual agents are driven by the utility maximization principle, the alternative picture that we have described is that the agents can be viewed as particles exchanging "wealth," instead of energy, and trading in wealth (energy) conserving two-body scattering, as in entropy maximization based on the kinetic theory of gases.³⁴ This qualitative analogy between the two maximization principles is not new – both economists and physicists had noted it in many contexts, but this equivalence has gained firmer ground only recently.³⁷

**FIG. 4.** (Color online) Example of a realistic wealth distribution, from Ref. 36. Continuous curve: wealth distribution obtained by simulations of a mixed population of agents, such that 1% of the agents have uniformly distributed saving propensities λᵢ ∈ (0, 1) and the other 99% of the agents have λᵢ = 0.2. Dotted curve: exponential wealth distribution ∝ exp(−*w*/⟨*w*⟩), with the same average wealth, plotted for comparison with the distribution in the intermediate-wealth region. Dashed curve: Pareto power law ∝ *w*⁻², plotted for comparison with the large-income part of the distribution.

---

## V. SUGGESTED PROBLEMS

The wealth exchange models, we have discussed are minimal and lend themselves to various generalizations and modifications to study the effect of additional features. Choose the kinetic exchange model, for instance, defined by: *w*ᵢ → *w*ᵢ − Δ*w*ᵢⱼ and *w*ⱼ → *w*ⱼ + Δ*w*ᵢⱼ, with Δ*w*ᵢⱼ = (1 − ε)*w*ᵢ − ε*w*ⱼ. Perform the simulations and check whether the corresponding equilibrium Boltzmann-Gibbs distribution *f*(*w*) = β exp(−β*w*), where β = 1/⟨*w*⟩ is reached, starting from any arbitrary initial distribution of *w* amongst the agents. Next, perform the simulations for *w*ᵢ → *w*ᵢ − Δ*w*ᵢⱼ and *w*ⱼ → *w*ⱼ + Δ*w*ᵢⱼ, when the form of Δ*w*ᵢⱼ or the dynamical equations are modified, as suggested in the following.

- **Different exchange rules:** Verify that the final equilibrium wealth distribution remains Boltzmann-Gibbs distribution, when employing the rule that at each step an arbitrary constant amount [Δ*w*ᵢⱼ = *w*₀] is exchanged, or at each step a fraction of the average wealth in the system is exchanged.²⁵ However, if instead the minimum wealth between the two agents is used as the exchanged amount [Δ*w*ᵢⱼ = min(*w*ᵢ, *w*ⱼ)], condensation of the total wealth in the hands of a single agent will take place.³⁸

- **Taxation on transactions:** Modify the dynamical equations by adding a term that takes as tax, a fixed amount of wealth δ*w*₀ or a fixed percentage of the wealth exchanged Δ*w*ᵢⱼ from agents *i* and *j*, and redistributes it uniformly among all the others.²⁵

- **Debt:** Modify the dynamical equations such that the agents are allowed to borrow or take loans up to a maximum amount *w*_max so that their wealth may become negative but not smaller than −*w*_max. This modification can be implemented by increasing the total wealth by an additional amount *w*_max.²⁵

- **Fixed saving:** Add to the model a fixed saving *w*₀ for each of the two agents, so that the total wealth is diminished by an amount 2*w*₀.³⁸

- **Many-agent interactions:** Set up a new dynamical rule in which wealth is redistributed in encounters between more than two agents, for example, among three agents *i*, *j*, and *k*. The other details of the transaction should be similar to that of a pair-wise transaction between agents *i* and *j*. Some care has to be taken to properly define the respective random fractions of wealth assigned to each agent to make the process symmetrical with respect to all the agents involved in the encounter.

---

## ACKNOWLEDGMENTS

We are grateful to all our collaborators and students. M.P. acknowledges financial support by the targeted financing project SF0690030s09 and by the Estonian Science Foundation through grant no. 9462.

\* marco.patriarca@kbfi.ee  
† anirban.chakraborti@ecp.fr

---

## REFERENCES

¹ L. Boltzmann, *Lectures on Gas Theory*, Dover, NY (1964).

² J. P. Sethna. *Statistical Mechanics*, Oxford University Press, Oxford (2006).

³ D. ter Haar, *Elements of Statistical Mechanics*, Butterworth-Heinemann, Oxford (1995).

⁴ A. Chakraborti, I. Muni Toke, M. Patriarca, and F. Abergel, "Econophysics review: II. Agent-based models," *Quantitative Finance* **11**, 1013–1041 (2011).

⁵ A. Chatterjee and B. K. Chakrabarti, "Kinetic exchange models for income and wealth distributions," *Eur. Phys. J. B* **60**, 135–149 (2007).

⁶ M. Lallouache, A. S. Chakrabarti, A. Chakraborti, and B. K. Chakrabarti, "Opinion formation in kinetic exchange models: Spontaneous symmetry-breaking transition," *Phys. Rev. E* **82**, 056112-1–5 (2010).

⁷ M. Patriarca, E. Heinsalu, and A. Chakraborti, "Basic kinetic wealth-exchange models: common features and open problems," *Eur. J. Phys. B* **73**, 145–153 (2010).

⁸ P. Ball, "The physical modelling of society: a historical perspective," *Physica A* **314**, 1–14 (2002).

⁹ L. Boltzmann, "Weitere Studien über das Wärmegleichegewicht unter Gasmolekulen," *Akad. Wiss. Wein* **66**, 275–370 (1872).

¹⁰ A. Chakraborti and M. Patriarca, "Gamma-distribution and wealth inequality," *Pramana J. Phys.* **71** (2), 233–243 (2008).

¹¹ M. Patriarca, A. Chakraborti, and K. Kaski, "Gibbs versus non-Gibbs distributions in money dynamics," *Physica A* **340**, 334–339 (2004).

¹² M. Patriarca, A. Chakraborti, and K. Kaski, "Statistical model with a standard gamma distribution," *Phys. Rev. E* **70**, 016104-1–5 (2004).

¹³ N. L. Johnson, S. Kotz, and N. Balakrishnan, *Continuous Univariate Distributions*, Wiley, New York (1994), Vol. 1.

¹⁴ M. Abramowitz and I. A. Stegun, *Handbook of Mathematical Functions*, Dover, New York (1972).

¹⁵ A. Dragulescu and V. M. Yakovenko, "Evidence for the exponential distribution of income in the USA," *Eur. Phys. J. B* **20**, 585–589 (2001).

¹⁶ A. Chakraborti, I. Muni Toke, M. Patriarca, and F. Abergel, "Econophysics review: I. Empirical facts," *Quantitative Finance* **11**, 991–1012 (2011).

¹⁷ J. Angle, "The surplus theory of social stratification and the size distribution of personal wealth," *Soc. Forces* **65**, 293–326 (1986).

¹⁸ J. Angle, "The inequality process as a wealth maximizing process," *Physica A* **367**, 388–414 (2006).

¹⁹ J. Angle, "Deriving the size distribution of personal wealth from 'the rich get richer, the poor get poorer'," *J. Math. Sociol.* **18**, 27–46 (1993).

²⁰ J. Angle, "The one-parameter inequality process," *Physica A* **367**, 388–414 (2006).

²¹ E. Bennati, "Un modello probabilistico per la distribuzione del reddito," in *Atti della Prima Riunione Scientifica della Società Italiana di Statistica*, 1978, pp. 1–14.

²² E. Bennati, "La distribuzione funzionale del reddito: un modello probabilistico," *Rivista di Politica Economica* **6**, 3–28 (1988).

²³ E. Bennati, "Un modello probabilistico per la distribuzione del reddito," *Statistica* **48**, 283–296 (1988).

²⁴ S. Ispolatov, P. L. Krapivsky, and S. Redner, "Wealth distributions in asset exchange models," *Eur. Phys. J. B* **2**, 267–276 (1998).

²⁵ A. Dragulescu and V. M. Yakovenko, "Statistical mechanics of money," *Eur. Phys. J. B* **17**, 723–729 (2000).

²⁶ A. Chakraborti and B. K. Chakrabarti, "Statistical mechanics of money: how saving propensity affects its distribution," *Eur. Phys. J. B* **17**, 167–170 (2000).

²⁷ M. Patriarca, A. Chakraborti, and G. Germano, "Influence of saving propensity on the power-law tail of the wealth distribution," *Physica A* **369**, 723–736 (2006).

²⁸ A. Dragulescu and V. M. Yakovenko, "Exponential and power-law probability distributions of wealth and income in the United Kingdom and the United States," *Physica A* **299**, 213–221 (2001).

²⁹ P. Sen, "Phase transitions in a kinetic model of opinion formation," *Phys. Rev. E* **84**, 042101 (2011).

³⁰ A. Chatterjee, B. K. Chakrabarti, and S. S. Manna, "Pareto law in a kinetic model of market with random saving propensity," *Physica A* **335**, 155–163 (2004).

³¹ G. Katona and J. Kertész, "Pareto's law and the power-law distribution of wealth in a stochastic exchange model," *Physica A* **387**, 1865–1871 (2008).

³² A. Ghosh, A. Chakraborti, and B. K. Chakrabarti, "A poverty threshold model of wealth distribution," *Physica A* **390**, 2830–2839 (2011).

³³ A. Chakraborti and M. Patriarca, "Gamma-distribution and wealth inequality," *Pramana J. Phys.* **71**, 233–243 (2008).

³⁴ M. Patriarca, A. Chakraborti, and K. Kaski, "Statistical model with a standard gamma distribution," *Phys. Rev. E* **70**, 016104 (2004).

³⁵ A. Chatterjee, S. Yarlagadda, and B. K. Chakrabarti, "Kinetic exchange models of income and wealth distributions," in *Econophysics of Wealth Distributions*, edited by A. Chatterjee, S