my_bot=ChatBot(name='SnakeBot', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
general_talk=[
    'Greetings Humanoid',
    'Hello!',
    'How is your life operating?',
    'Are you good?',
    'I am SnakeBot1.0',
    'I\m a program. I have no emotions :l',
    'Sorry to hear that. Can I help?',
    'Wow, Imagine being salty'
    'That is magnificent'
]

list_trainer=ListTrainer(my_bot)
for item in (general_talk):
    list_trainer.train(item)

    >>> print(my_bot.get_response("hi"))
    How is your life operating?
    >>> print(my_bot.get_response("good"))
    That is magnificent
    >>> print(my_bot.get_response("what's your name?"))
    I am SnakeBot1.0
    >>> print(my_bot.get_response("you are bad"))
    Wow, Imagine being salty
    >>> print(my_bot.get_response("how are you"))
    Im a program. I have no emotions :l