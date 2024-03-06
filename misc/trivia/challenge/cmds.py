import discord
import random
from os import environ
from db import get_score, add_one, remove_one, reset_score, add_attempt, get_last_unsolved_attempt, solve_attempt
import base64


GIFT = environ.get("GIFT", "A pat on the back")


async def score(channel, server_id):
    await channel.send(f"Your score is {get_score(server_id)}")


async def help(channel):
    embed = (
        discord.Embed(
            title="Trivia Challenge - Help",
            description=(
                """Welcome to the Trivia Challenge! Your mission: correctly answer 100 questions to get a gift. But be aware: one wrong answer will reset your score to zero. Think you have what it takes?\n
                !help - Show this message
                !trivia - Get a trivia question (There are 4 types of questions)
                !score - Get your score
                !submit <answer> - Submit an answer
                """
            ),
            colour=discord.Colour.blue(),
        )
    )
    await channel.send(embed=embed)


async def submit(channel, server_id, answer):
    attempt = get_last_unsolved_attempt(server_id)
    if not attempt:
        await channel.send(f"Please get a question first")
        return
    if answer.lower() == attempt[2].lower():
        add_one(server_id)
        if get_score(server_id) == 100:
            await channel.send(f"Correct! here's your gift: {GIFT}\nHave fun with your gift hacker!!")
            return
        await channel.send(f"Correct! Your score is now {get_score(server_id)}")
    else:
        reset_score(server_id)
        await channel.send(f"Wrong! Your score is now {get_score(server_id)}")
    solve_attempt(attempt[0])
    return


def generate_polynomial(degree, coefficients=None):
    if coefficients is None:
        coefficients = [random.randint(-10, 10) for _ in range(degree + 1)]

    def polynomial(x):
        result = 0
        for i, coeff in enumerate(coefficients):
            result += coeff * (x ** i)
        return result
    coefficients_str = ' + '.join(f"{coeff}x^{i}" for i,
                                  coeff in enumerate(coefficients) if coeff != 0)
    equation_str = f"Equation: f(x) = {coefficients_str}"
    return polynomial, equation_str


def random_enc():
    length = random.randint(15, 50)
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    answer = ''.join(random.choice(characters) for _ in range(length))
    encoding = random.choice(['binary', 'hex', 'base64'])
    final = ""
    if encoding == 'binary':
        final = ''.join(format(ord(char), '08b') for char in answer)
    elif encoding == 'hex':
        final = answer.encode().hex()
    elif encoding == 'base64':
        final = base64.b64encode(answer.encode()).decode()
    return answer, final


def generate_matrix():
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],]
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    matrix[x-1][y-1] = 1
    return matrix, (x, y)


def generate_knapsack_instance(num_items, max_weight):
    items = []
    for i in range(num_items):
        weight = random.randint(1, max_weight)
        value = random.randint(1, 100)
        items.append((weight, value))
    return items


def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))


async def trivia(channel, server_id) -> None:
    attempt = get_last_unsolved_attempt(server_id)
    if attempt:
        await channel.send(f"Please answer the previous question first")
        return
    if get_score(server_id) >= 100:
        await channel.send(f"Congratulations! You have already won your gift")
        return
    rnd = random.randint(0, 3)
    if rnd == 0:
        title = "Are you a math wiz?"
        polynomial, equation_str = generate_polynomial(random.randint(3, 8))
        x = random.randint(-100, 100)
        question = f"Given the following polynomial, what is f({x})?\n{equation_str}"
        correct_answer = str(polynomial(x))
    elif rnd == 1:
        title = "Cypher, what's the message?"
        correct_answer, question = random_enc()
    elif rnd == 2:
        title = "Welcome to the matrix!"
        matrix, (x, y) = generate_matrix()
        question = f"Find the coordinates (x,y) of the 1 in the following matrix:\n" + \
            '\n'.join([' '.join(map(str, row)) for row in matrix]) + \
            "\nP.S. The first row and column are 1 and 1, respectively."
        correct_answer = "(" + str(x) + "," + str(y) + ")"
    elif rnd == 3:
        title = "Heist time! grab the most valuable items!"
        capacity = random.randint(10, 100)
        items = generate_knapsack_instance(random.randint(3, 15), capacity)
        question = f"Given the following items, what is the maximum value you can carry with a knapsack of capacity {capacity}?\n" + \
            '\n'.join(
                [f"Item {i+1}: weight {w}, value {v}" for i, (w, v) in enumerate(items)])
        correct_answer = str(knapSack(capacity, [w for w, _ in items], [
                             v for _, v in items], len(items)))
    embed = discord.Embed(
        title=title, description=question, color=discord.Colour.blue(), type="rich")
    await channel.send(embed=embed)
    add_attempt(server_id, question, correct_answer)
