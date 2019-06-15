Identify data structures
========================

General idea
------------

Once the code "works", that its side-effects are identified and isolated and that it's core code is tested we can be reasonably confident that it's going to do what we intended. It's time to ask ourselves how to build from there. Although it's certainly not mandatory, we spent time writing this code, and it would be great to be able to justify that investment over time.

There are two main ways this code will likely be built upon. Either it will evolve, to follow the evolving understanding we'll acquire of its impact, or we'll extend it to cover aspects of the domain that we didn't foresee. Or both! In any case, not all sections of the code will change together, and the better we understand that, the simpler, nicer —and cheaper— change will become.

One way to get that understanding is looking at our data.

Where to start?
---------------

Pick the information you start with, that might be an API call, some user input, or database query, and take a moment to observe how you represent it. Describe it and name it.

> The purpose of a program is to describe a computational process that consumes some information and produces new information. [...] All this information comes from a part of the real world—often called the program’s _domain_—and the results of a program’s computation represent more information in this domain. [...] For a program to process information, it must turn it into some form of _data_ in the programming language; then it processes the data; and once it is finished, it turns the resulting data into information again. — (source: [How to Design Programs][htdp2e])

  [htdp2e]: https://htdp.org/2019-02-24/part_one.html#%28part._sec~3adesign-func%29


For example, the information you work with might be the current temperature. The way you represent it at the input of your program is using an [`int`](https://docs.python.org/2/library/types.html#types.IntType) in Python, _that_ is your data.

```python
# A temperature is an int, it represents Fahrenheit degrees.
current_temp = 71 # is a temperature

# A time is an int, it represents a Unix Epoch.
bob_time_of_birth = 74 # is a time (Jan. 1st, 1970 at 00:01 UTC)
# It looks a lot like a temperature, and that's okay — as long as it's clear it's not.
```

From data to namespaces
-----------------------

### Naming data

Naming is hard, and you might find different representations for similar information in your program. At first, that might look like a challenge, but it is an opportunity to identify domains (sub-domains, if you want) within your program.

For example, you may write a program with the purpose to help you choose transportation mode for a given journey. You first get the data from a map service provider:

```python
# journey_planner.py

# A journey is a tuple of two ints, they represent the distance in meters and the altitude gain in meters.
home_to_work = get_journey_from_map_service(home, work)
home_to_work
# => (1200,75) is a journey ①
```

- ① `journey` seems like an appropriate name given the purpose statement of the program.

----

But for you, the journey is definitely not the same if walking under the sun or under the rain. You'd take the bus if it's raining, even for a short distance. And you need that information to feed into the transport mode selector.

```python
# journey_planner.py

# [...]

# A weather is a string, either 'sunny' or 'raining'.
current_weather = 'raining' # is a weather

# A "journey with weather" is a tuple of two ints and a string.
# They represent the distance in meters, the altitude gain in meters and the weather.
home_to_work = (2400, 30, 'sunny') # is a "journey with weather" ②

# Expects a "journey with weather" as an argument.
recommend_transportation_mode_for_journey(home_to_supermarket)
```

- ② `journey with weather` is less obviously a good name. How many things could we add before things get confusing? To me, this is a [code smell](https://www.martinfowler.com/bliki/CodeSmell.html).

We already have a `journey` though (①), we can't really give the same name to different things can we?

The key idea here is that if the weather service and your transportation recommendation function have different meanings for the same word, it is because their context is different enough that they need different data to deal with the same information. It might be interesting to treat them as different domains.

### Naming domains

One way to acknowledge domains is naming them, let's try and go with `map_service` and `journey_planner`.

```python
# journey_planner.py ⑤

# A map_service_journey is a tuple of two ints, they represent the distance in meters and the altitude gain in meters.
home_to_work = get_journey_from_map_service(home, work)
home_to_work
# => (1200,75) is a map_service_journey ③

# [...]

# A journey_planner_journey is a tuple of two ints and a string.
# They represent the distance in meters, the altitude gain in meters and the weather.
home_to_work = (2400, 30, 'sunny') # is a journey_planner_journey ②

# Expects a journey_planner_journey as an argument.
recommend_transportation_mode_for_journey(home_to_supermarket)
```

- ③ Same as ① with the data type name changed to `map_service_journey`
- ④ Arr, `journey_planner_journey` is not a great name...
- ⑤ ...but notice the context, we'll fix that immediately.

----

```python
# journey_planner.py

# A map_service_journey is a tuple of two ints, they represent the distance in meters and the altitude gain in meters.
home_to_work = get_journey_from_map_service(home, work)
home_to_work
# => (1200,75) is a map_service_journey ⑦

# [...]

# A journey is a tuple of two ints and a string.
# They represent the distance in meters, the altitude gain in meters and the weather.
home_to_work = (2400, 30, 'sunny') # is a journey ⑥

# Expects a journey as an argument.
recommend_transportation_mode_for_journey(home_to_supermarket)
```

- ⑥ In the context of the `journey_planner` module, we might as well call this type `journey`. Now our data types read fine and are not ambiguous anymore.
- ⑦ If you're thinking "could this be called `journey` in the `map_service` context?" you're on a good track!

There are two interesting things to notice at this point: the relationship between domains and what we'll call _namespaces_, And the relationship between those and change.

### Domains and namespaces

The idea behind a **namespace** is that in different spaces, the same words can have different meanings. Family names can be thought of as namespaces for example. In Python, [module](https://docs.python.org/3/tutorial/modules.html) names can be used as namespaces. Let's do this.

```python
# map_service.py

def get_journey(): # ⑨ — formerly: get_journey_from_map_service()
  pass

# A journey is a tuple of two ints, they represent the distance in meters and the altitude gain in meters.
home_to_work = get_journey(home, work)
home_to_work
# => (1200,75) is a journey ⑧
```

```python
# journey_planner.py

import map_service # ⑩

home_to_work = map_service.get_journey(home, work) # ⑪
home_to_work
# => (1200,75) is a map_service_journey ⑫

# [...]

# A journey is a tuple of two ints and a string.
# They represent the distance in meters, the altitude gain in meters and the weather.
home_to_work = (2400, 30, 'sunny') # is a journey

# Expects a journey as an argument.
recommend_transportation_mode_for_journey(home_to_supermarket)
```

- ⑧ In the `map_service` context (namespace), `journey` is unambiguous.
- ⑨ Notice that the name `get_journey_from_map_service()` also hinted at the `map_service` domain.
- ⑩ We now see clearly that `journey_planner` has a dependency on `map_service`.
- ⑪ notice how the namespace makes names unambiguous.
- ⑫ well in this context, we'll likely keep talking about `map_service_journey`. (In other languages —Golang for example— we might define a _type_ as code in the `map_service` namespace and refer to it as `map_service.Journey`, but in our case it's only text.)

When to stop?
-------------

Remains for us to talk about the relationship between domains and namespaces on one hand, and change on the other. That is pretty quick: suffice to say that _often_, things that belong to the same domain tend to change together. If our map service starts using miles instead of kilometers to define a journey, it is likely that a few of the functions that it provides will change accordingly.

As a rule of thumb, we want things that change together to be grouped together, so that we know where to look for updates when that happens. Modules being both namespaces and separate files in Python are great for that.

But **not all domains are equal**. Sometimes, you'll be able to distinguish between aspects of your program that you could find a name for, consider as separate domains and split into modules — but that are very unlikely to change independently from one another!

At that point, it is wise to ask what benefit you get out of splitting them apart. Although intellectually you might be able to tell the difference between them, maybe that distinction is not relevant _in the context of your program_. That's the right moment to stop staring at your data and to move to the next step. Remember: don't do more than needed.
