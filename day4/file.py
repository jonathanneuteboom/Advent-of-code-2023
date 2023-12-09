import re


def parseMap(startIndex: int, endIndex: int, lines: list[str]):
    rules = []
    for i in range(startIndex, endIndex):
        matches = re.search(r"(\d+) (\d+) (\d+)", lines[i]).groups()
        newRule = (int(matches[0]), int(matches[1]), int(matches[2]))
        rules.append(newRule)

    return rules


def parseFile(filename: str):
    file = open(filename, "r")
    lines = file.read().splitlines()
    seeds = list(
        map(
            lambda x: int(x), re.search(r"seeds: (.*)", lines[0]).groups()[0].split(" ")
        )
    )

    maps = {}

    mapTypes = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]

    for mapType in mapTypes:
        startIndex = lines.index(f"{mapType} map:")
        endIndex = lines.index("", startIndex)
        maps[mapType] = parseMap(startIndex + 1, endIndex, lines)

    return {"seeds": seeds, "maps": maps}


def getNewValue(value: int, map: list[(int, int, int)]):
    for mapItem in map:
        targetStart = mapItem[0]
        sourceStart = mapItem[1]
        range = mapItem[2]
        if sourceStart <= value and value <= sourceStart + range:
            difference = value - sourceStart
            return targetStart + difference

    return value


def convert(input: list[int], map: list[(int, int, int)]):
    result = []
    for value in input:
        result.append(getNewValue(value, map))

    return result


result = parseFile("day4/input.txt")
maps = result["maps"]
intermediary = convert(result["seeds"], maps["seed-to-soil"])
intermediary = convert(intermediary, maps["soil-to-fertilizer"])
intermediary = convert(intermediary, maps["fertilizer-to-water"])
intermediary = convert(intermediary, maps["water-to-light"])
intermediary = convert(intermediary, maps["light-to-temperature"])
intermediary = convert(intermediary, maps["temperature-to-humidity"])
intermediary = convert(intermediary, maps["humidity-to-location"])
print(f"Lowest: {min(intermediary)}")
