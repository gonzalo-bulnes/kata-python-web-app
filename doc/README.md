An approach to make code "production-ready"
===========================================

There is no "one true way" to write code or make it production-ready. What _production-ready_ means will highly depend on what the code does and the context in which you will use it. However, it is generally useful to try and prioritise among all the things that you could do to increase the level of confidence that you have in your code, and approach that task in a systematic way.

> The general rule of thumb is: **don't do more than needed**. The sooner your code is in production, the sooner it actually starts being useful. You are only judge of what is _needed_, and it is a difficult question to answer. Different people around you will have different thoughts about what that means. Try to stay open-minded about it, accept that you might not be fully comfortable with the code you ship to production, but be reasonable, think through the consequences and don't put yourself in a position where you'd be tempted to deny responsibility for what you ship — because you _are_ ultimately responsible for what the code you write does.
>
> I'll do my best to help. Now take a breath, it takes practice, but you can do it! ; ) — [GB](https://github.com/gonzalo-bulnes)

Two different kinds of steps
----------------------------

While most steps in the list below aim at increasing your understanding of your code and helping you gain confidence that either you or your teammates will be able to evolve it as needed, the first step is a little different. It has mostly not to do with your code, or the direct effects of your code.

The first step of the list —[Store the configuration in the environment][config]— is arbitrary in that it has first of all to do with security. The security of the information you use to do your job, and that could be used for different purposes. That is indeed why it's the first step in my list. Leaving credentials behind is frowned-upon, with reason! Don't do it, it's not difficult to fix.

And that first step as it is described will also put you in a good position to deploy your code and will make you friends in your development operations team (and if that team is you, you'll love yourself for that!) It's a good investment.

Let's get started!
------------------

  [config]: ./store_config_in_the_environment.md
  [side-effects]: ./identify_and_start_isolating_side_effects.md
  [data]: ./identify_data_structures.md
  [emotions]: ./the_emotional_stuff.md
  [release]: ./release_early_release_often.md

1. [Store the configuration in the environment][config]
1. [Identify side-effects and start isolating them][side-effects]
1. [Identify data structures and namespaces][data]
1. [The emotional stuff][emotions]
1. [Release early, release often][release]
