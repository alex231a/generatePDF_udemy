from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='p', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", border=0, ln=1, align='L')
    pdf.line(10, 21, 200, 21)

    pdf.ln(260)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", border=0, ln=1, align='R')

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        pdf.ln(270)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=f"{row['Topic']}", border=0, ln=1, align='R')
pdf.output('output.pdf')
