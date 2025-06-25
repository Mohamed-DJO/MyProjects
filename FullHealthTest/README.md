# Full Health Test
#### Video Demo:  <https://youtu.be/m0FCRAKuW_E>
#### Description:
This Python program generates a personalized health report in PDF format using the FPDF library. It collects user input via the command line for several health metrics, including:

- Name
- Height (in meters)
- Weight (in kilograms)
- Age (in years)
- Blood Pressure (systolic, in mm Hg)
- Blood Sugar (fasting, in mg/dL)
- Sex (male/female)

Based on these inputs, the program calculates and analyzes:

- **Body Mass Index (BMI)** — categorized as Underweight, Normal, or Overweight with color-coded indicators.
- **Blood Pressure classification** — Normal, Elevated, Hypertension Stages 1 and 2, or Hypertensive Crisis, each shown in distinct colors.
- **Blood Sugar levels** — evaluated differently according to age groups, marked as Normal or Not Normal.
- **Basal Metabolic Rate (BMR)** — calculated using the Mifflin-St Jeor equation adjusted for sex, providing an estimated daily calorie requirement.

The program outputs all these findings to a styled PDF named `full_health_test.pdf`, positioning text clearly with fonts and colors. Finally, it includes a randomly selected motivational health quote.

### How to Use:

Run the script in a terminal or command prompt. You will be prompted to enter each required field one by one.

After providing valid inputs, the program generates the PDF report automatically.

### Function Overview:

- `main()`: Manages user input collection, validation, and calls all analysis and PDF generation functions.
- `ibm(weight, height)`: Calculates BMI and adds a color-coded status to the PDF.
- `pressure(blood_pressure)`: Classifies blood pressure levels with color indicators.
- `sugar(blood_sugar, age)`: Checks blood sugar normality based on age-specific ranges.
- `calories(weight, height, age, sex)`: Calculates BMR using sex-specific formulas.
- `quotes()`: Adds a random motivational health quote to the PDF.

### Technical Details:

- Uses the **FPDF** Python library to create and format the PDF.
- Text placement uses `set_y()` for vertical positioning and `cell()` for adding content.
- Text colors are adjusted via RGB values to highlight health statuses.
- The PDF page is A4 size, portrait orientation.

This project is ideal for health professionals or individuals looking to create quick, clear health summaries with minimal user input and automated report generation.

