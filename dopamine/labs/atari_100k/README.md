
#### Labs: Atari 100k
This directory provides code for running experiments on the [Atari 100k][simple]
benchmark where agents are evaluated after training only for 100k environment
steps (400k frames of interaction).

* To get started, we release JAX implementations of following agents:
 * [DER][der] (Data Efficient Rainbow)
 * [OTRainbow][otr] (Over-trained Rainbow)
 * [DrQ][drq] (Data-regularized Q)

All of these agents are based on the [full rainbow][full_rainbow] agent in Dopamine
and can be instantiated using the gin configs provided in this directory. For evaluation, we report scores averaged over 100 episodes after training.

##### References
[Kaiser, Lukasz, et al. "Model-based reinforcement learning for atari." arXiv preprint arXiv:1903.00374 (2019).][simple]

[van Hasselt, H. P., Hessel, M., & Aslanides, J. (2019). When to use parametric models in reinforcement learning?. Advances in Neural Information Processing Systems, 32, 14322-14333.][der]

[Kielak, K. (2020). Importance of using appropriate baselines for evaluation of data-efficiency in deep reinforcement learning for Atari. arXiv preprint arXiv:2003.10181.][otr]

[Yarats, D., Kostrikov, I., & Fergus, R. (2020, September). Image Augmentation Is All You Need: Regularizing Deep Reinforcement Learning from Pixels. In International Conference on Learning Representations.][drq]

[der]: https://arxiv.org/abs/1906.05243
[otr]: https://arxiv.org/abs/2003.10181
[drq]: https://arxiv.org/abs/2004.13649
[simple]: https://arxiv.org/abs/1903.00374
[full_rainbow]: https://github.com/google/dopamine/tree/master/dopamine/jax/agents/full_rainbow