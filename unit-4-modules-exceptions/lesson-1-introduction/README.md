# Modules and Packages

We write a lot of code. **A LOT**. The [Django Web Framework](https://www.djangoproject.com/) entire project's size is **39 Megabytes**, distributed across **2439 files**. When you start coding, you usually start with a single `main.py` file. But, as the code starts to grow, you feel the need of splitting it between different files (or even directories) to keep it a little bit more organized. Imagine those 39MB of Django code in a single file. That'd be a file with 318,169 Lines of Code.

## Python modules

A _module_ in Python is simply a valid python file (`*.py` extension) with code inside. Modules are used to organize your code. In a game project you might have all the models in `models.py` and all the game rules in `rules.py` and all the characters in `characters.py`.

Once you've split your code among multiple files, you need to make use of that. For example, the module `characters.py` might need to use a function defined in `rules.py`. You can have access to functions or variables defined in other modules (strictly expressed as _other modules' members_) by **importing** those members with the `import` statement.

## Importing

Suppose you have 2 modules; one containing characters for your game:

**characters.py**
```python
def make_warrior(name, health, power):
    pass

Ragnar = make_warrior('Ragnar Lodbrok', 70, 98)
Vercingetorix = make_warrior('Vercingetorix', 120, 89)
```

and another one containing the code that makes the warriors fight:

**main.py**
```python
game = setup_game('Fight 1')
game.start_fight(Ragnar, Vercingetorix)
```

How do you access those variables (`Ragnar` and `Vercingetorix`) from within `main.py`? The answer is simple, you have to **_import_** them. Here's how we could change `main.py` to correctly import those warriors:

```python
from characters import Ragnar, Vercingetorix
# ... more code...
game = setup_game('Fight 1')
game.start_fight(Ragnar, Vercingetorix)
```

The import statement "searches" for a python file named `characters.py` within the current directory, and if it finds it, it'll "load" the code (it'll scan and execute the whole `characters.py` file) and finally, it'll make the requested _members_ (`Ragnar` and `Vercingetorix`) available to the `main.py` module. It's pretty much the same as those members would have been originally defined inside `main.py`, they're fully available in whatever module they're imported.

There are a few different ways of importing code in Python, let's compare them all:

**`from characters import Ragnar, Vercingetorix`**

```python
from characters import Ragnar, Vercingetorix
# ... more code...
game = setup_game('Fight 1')
game.start_fight(Ragnar, Vercingetorix)
```

This is the same code as our previous example. In this case we're explicitly indicating what members we need to access, and after they're imported, we can just use them with their own names. As said before, there's no difference between importing them or just defining them in the `main.py` file.

**`import characters`**

```python
# main.py
import characters  # 1

# ... more code...
game = setup_game('Fight 1')
game.start_fight(characters.Ragnar, characters.Vercingetorix)  # 2
```

In this case we're not explicitly importing "individual" members, but we're importing the entire `characters.py` module (_1_). Once you've imported the entire module, you can access any internal member by prepending the name of the module (_2_) with the syntax: `module.member`. 

This method has a clear advantage: you always know where those members came from. It'll make more sense in the following [comparison section](#which-one-is-better-comparing-different-import-mechanisms).

**`from characters import *`**

```python
from characters import *  # 1
# ... more code...
game = setup_game('Fight 1')
game.start_fight(Ragnar, Vercingetorix)
```

This method is usually called _"import star"_. In this case you're using the special _asterisk_ (or _star_) character to denote that you want to import **every** member from `characters.py`. You can then access those members directly as if they'd have been imported with the other `from module import Ragnar` syntax (_2_).

This method is not usually recommended. See next [section](#which-one-is-better-comparing-different-import-mechanisms) for details.

**`from characters import Ragnar as R, Vercingetorix as V`**

```python
from characters import Ragnar as R, Vercingetorix as V
# ... more code...
game = setup_game('Fight 1')
game.start_fight(R, V)
```

This is usually referred as using "aliases". As you can imagine, we're importing the regular members `Ragnar` and `Vercingetorix` from `characters.py` but we're giving them special "names", so we can reference them differently later. Aliases are usually employed when two members from different models have the same names, and you need to differentiate them to avoid name conflicts. Example:

```python
from characters import Ragnar as Ragnar_Game
from tv_shows import Ragnar as Ragnar_Show
```

**`import characters as c`**

```python
import characters as c  # 1

# ... more code...
game = setup_game('Fight 1')
game.start_fight(c.Ragnar, c.Vercingetorix)  # 2
```

Aliases can also be used to import entire modules. They work in the same way as our previous example: once you set the alias, you reference that module by that special alias (_1_). Whenever you need to use a member of that module, you just prepend the alias name (_2_).

This is usually employed for modules with long names that are commonly used, so you (and other coders) are generally aware that `c` means `characters`.

## Which one is better? Comparing different import mechanisms.

This is obviously extremely subjective; most of these differences should be analyzed in a case by case basis. But we could generally agree on:

**`import module` is good**

The main advantage of this way of importing is that you're always aware of the origin of the member you're using. Take [this code from the Django project](https://github.com/django/django/blob/87c76aa116ef49be2d6ff3ecf2fec37414638246/django/core/handlers/wsgi.py#L86) as an example; the name `lookup` for a function is pretty general. Anything can be named "`lookup`". But, as it's being used with the name of the module prepended, it's obvious where it's coming from.

The disadvantage of this approach is its verbosity. If you have members that are used many times within another module, prepending them with the module name is sometimes overkilling.

**`from module import A` is the most popular choice** 

This is the most common form and you can rest assured that it'll be just fine 99% of the times. You just need to be careful not to have name conflicts (use aliases for those cases) and that you're not importing something with a name that's too generic (like `lookup`) and not commonly used.

Basically, what you want to avoid is other developer reading through your code, stumbling upon a function (or other member), and being completely clueless about its origin.

**`from module import *` (import star) is BAD** 

To be fair, it's not little import star's fault. We usually use it incorrectly. Strictly, import star isn't bad, but it's dangerous and should be used wisely and carefully.

When you do `from module import *` you're importing **EVERYTHING**. Check the following example:

Module `module_a.py`:

```python
# module_a.py
import time  # 1
VARIABLE_A = 'Hello World'
# both `time` and `VARIABLE_A` will be "exposed"
```

`main.py`:

```python
# main.py
from datetime import time  # 2
from module_a import *  # 3
print(time)  # 4
```

What `time` will `main.py` print?

In this case, the `time` imported in `main.py` in _(2)_ gets overwritten by the one brought from `module_a` (originally imported in _(1)_). Basically, when you did `import *` you meant **EVERYTHING**; every single member that can be exposed will be imported in `main.py`, and this is obviously dangerous. If you're distracted or you just don't know what `module_a.py` contains, you'll end up stepping over your own imports.

As we said, import star is not just plain "bad", you just need to be careful when using it. There's actually a mechanism to prevent the overwrite issue previously noted (we'll explore it in more advanced sections).

## Biggest import gotcha

What usually surprises our students is the fact that "importing a module" just plainly executes all the code in that module. That means that, for example, any "operation" happening in that module, will be executed normally as if you'd been running that module directly. Example:

```python
# emails.py
DEFAULT_SUBJECT = "Welcome!" # 1
# ... some code ... 
send_email('test@rmotr.com', DEFAULT_SUBJECT)  # 2
```

```python
# main.py
from emails import DEFAULT_SUBJECT # 3
```

In this case, the module `email.py` defines the variable `DEFAULT_SUBJECT` (_1_) that we want to import in (_3_). But, as we import `DEFAULT_SUBJECT`, we're also executing the whole content of `emails.py` and with it, we're also executing the line in (_2_), which (apparently) sends an email. That means that, every time you run `main.py`, a new email will be sent due to the import statement.

