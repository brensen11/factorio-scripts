from data import technologies
import sys
import json

def science_packs_to_code(science_packs: list[str]) -> str:
    science_letters = ""
    for science_pack in science_packs:
        match science_pack:
            case "automation-science-pack":
                science_letters += 'R'
            case "logistic-science-pack":
                science_letters += 'G'
            case "chemical-science-pack":
                science_letters += 'B'
    return science_letters


def calculate_research_total(research, totals = {}):
    unit = research.get('unit')
    research_trigger = research.get('research_trigger')

    prereqs = research.get('prerequisites')
    if prereqs:
        for prereq in prereqs:
            totals = calculate_research_total(technologies[prereq], totals)

    if unit:
        science_letters = science_packs_to_code([u[0] for u in unit['ingredients']])
        time = unit['time']
        count = unit['count']
        if not totals.get(science_letters):
            totals[science_letters] = {}
        if totals[science_letters].get(time):
            totals[science_letters][time] += count
        else:
            totals[science_letters][time] = count
        
    elif research_trigger:
        if totals.get('other'):
            totals['other'].append(research_trigger)
        else:
            totals['other'] = [research_trigger]
    print(f"TOTALS: {totals}\n\n")
    return totals


def main():
    # Check if a filename was provided
    if len(sys.argv) < 2:
        print("Usage: python research.py <research-name>")
        sys.exit(1)

    # Get the filename from the list of arguments
    research_name = sys.argv[1]
    print(f'totaling cost on: {research_name}')
    research = technologies.get(research_name)
    total = calculate_research_total(research)

    with open('research.json', 'w') as f:
        json.dump(total, f)

if __name__ == "__main__":
    main()