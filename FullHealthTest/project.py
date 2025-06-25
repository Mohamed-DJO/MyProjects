import sys
from fpdf import FPDF
import random

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_y(20)
pdf.set_font("Arial", size=48)
pdf.cell(0, 10, "Full Health Test", align='C')

def main():
    try:
        name = input("Name: ")
        pdf.set_y(30)
        pdf.set_font("Arial", size=21)
        pdf.cell(0, 10, f"Name: {name}", align='C')
    except ValueError:
        sys.exit()

    try:
        height = float(input("Height(m): "))
        pdf.set_y(40)
        pdf.set_font("Arial", size=21)
        pdf.cell(0, 10, f"Height: {height}m", align='C')
    except ValueError:
        sys.exit()

    try:
        weight = float(input("Weight(Kg): "))
        pdf.set_y(50)
        pdf.set_font("Arial", size=21)
        pdf.cell(0, 10, f"Weight: {weight}Kg", align='C')
    except ValueError:
        sys.exit()

    try:
        age = int(input("Age: "))
        pdf.set_y(60)
        pdf.set_font("Arial", size=21)
        pdf.cell(0, 10, f"Age: {age} year-old", align='C')
    except ValueError:
        sys.exit()

    try:
        blood_pressure = int(input("Blood Pressure(mm Hg): "))
        pdf.set_y(70)
        pdf.set_font("Arial", size=21)
        pdf.cell(0, 10, f"Blood Pressure: {blood_pressure}mm Hg", align='C')
    except ValueError:
        sys.exit()

    try:
        blood_sugar = int(input("Blood Sugar(mg/dl): "))
        pdf.set_y(80)
        pdf.set_font("Arial", size=21)
        pdf.cell(0, 10, f"Blood Sugar: {blood_sugar}mg/dl", align='C')
    except ValueError:
        sys.exit()

    sex = input('Sex(male/female): ')
    while sex.lower() not in ['male', 'female']:
        sex = input('Sex(male/female): ')

    ibm(weight, height)
    pressure(blood_pressure)
    sugar(blood_sugar, age)
    calories(weight, height, age, sex)
    quotes()

    pdf.output("full_health_test.pdf")


def ibm(weight, height):
    ibm = weight / height**2
    pdf.set_y(90)
    pdf.set_font("Arial", size=21)
    if 0 <= ibm < 18.5:
        pdf.set_text_color(255, 255, 0)
        pdf.cell(0, 10, f"Your IBM: {ibm:.1f}kg/m² Underweight!!!", align='C')
    elif 18.5 <= ibm < 25:
        pdf.set_text_color(0, 255, 0)
        pdf.cell(0, 10, f"Your IBM: {ibm:.1f}kg/m² Normal (OK)", align='C')
    else:
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, f"Your IBM: {ibm:.1f}kg/m² Overweight!!!", align='C')
    return ibm


def pressure(blood_pressure):
    bp = round(blood_pressure)
    pdf.set_y(100)
    pdf.set_font("Arial", size=21)
    if bp < 120:
        pdf.set_text_color(0, 255, 0)
        pdf.cell(0, 10, f"Your Blood Pressure: {bp}mm Hg Normal", align='C')
        return 1
    elif 120 <= bp < 129:
        pdf.set_text_color(255, 255, 0)
        pdf.cell(0, 10, f"Your Blood Pressure: {bp}mm Hg Elevated", align='C')
        return 2
    elif 129 <= bp < 139:
        pdf.set_text_color(255, 153, 51)
        pdf.cell(0, 10, f"Your Blood Pressure: {bp}mm Hg HIGH BLOOD PRESSURE Stage 1", align='C')
        return 3
    elif 139 <= bp <= 179:
        pdf.set_text_color(255, 128, 0)
        pdf.cell(0, 10, f"Your Blood Pressure: {bp}mm Hg HIGH BLOOD PRESSURE Stage 2", align='C')
        return 4
    else:
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, f"Your Blood Pressure: {bp}mm Hg HYPERTENSIVE CRISIS (consult your doctor)", align='C')
        return 5


def sugar(blood_sugar, age):
    pdf.set_y(110)
    pdf.set_font("Arial", size=21)
    if age < 13 or 20 <= age <= 59:
        if 70 <= blood_sugar <= 100:
            pdf.set_text_color(0, 255, 0)
            pdf.cell(0, 10, f"Your Blood Sugar: {blood_sugar}mg/dl Normal", align='C')
            return 1
        else:
            pdf.set_text_color(255, 0, 0)
            pdf.cell(0, 10, f"Your Blood Sugar: {blood_sugar}mg/dl Not Normal", align='C')
            return 2
    elif 13 <= age <= 19 or age >= 60:
        if 70 <= blood_sugar <= 105:
            pdf.set_text_color(0, 255, 0)
            pdf.cell(0, 10, f"Your Blood Sugar: {blood_sugar}mg/dl Normal", align='C')
            return 3
        else:
            pdf.set_text_color(255, 0, 0)
            pdf.cell(0, 10, f"Your Blood Sugar: {blood_sugar}mg/dl Not Normal", align='C')
            return 4


def calories(weight, height, age, sex):
    pdf.set_y(120)
    pdf.set_font("Arial", size=21)
    pdf.set_text_color(128, 128, 128)
    if sex.lower() == 'male':
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
        pdf.cell(0, 10, f"Your BMR: {bmr:.1f} (Male)", align='C')
    else:
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161
        pdf.cell(0, 10, f"Your BMR: {bmr:.1f} (Female)", align='C')
    return bmr


def quotes():
    quotes = [
        '"Take care of your body. It\'s the only place you have to live." - Jim Rohn',
        '"Health is not valued until sickness comes." - Thomas Fuller',
        '"A healthy outside starts from the inside." - Robert Urich'
    ]
    pdf.set_y(130)
    pdf.set_font("Arial", size=21)
    pdf.set_text_color(128, 128, 128)
    quote = random.choice(quotes)
    pdf.cell(0, 10, f"Quote: {quote}", align='C')
    return quote


if __name__ == '__main__':
    main()

