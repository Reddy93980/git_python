import random


def generate_story() -> str:
    explorer = random.choice(["a curious robot", "a sleepy wizard", "a brave penguin"])
    location = random.choice(["the moonlit forest", "an underwater city", "a floating library"])
    discovery = random.choice(["a map that changes every hour", "a tiny singing dragon", "a door to yesterday"])
    twist = random.choice(
        [
            "It turned out to be exactly what they needed.",
            "It immediately asked for a cup of tea.",
            "Nobody believed the story, but the stars did.",
        ]
    )

    return (
        f"One evening, {explorer} wandered into {location}. "
        f"There, they discovered {discovery}. {twist}"
    )


if __name__ == "__main__":
    print(generate_story())