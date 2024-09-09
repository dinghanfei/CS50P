from fpdf import FPDF

class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.create_shirt()

    @classmethod
    def get_name(cls):
        name = input("Name: ").strip()
        return cls(name)

    def create_shirt(self):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=False, margin = 0) # 防止自动换页
        pdf.add_page()

        pdf.set_font("Helvetica", "B", size=50)
        pdf.cell(0, 50, text="CS50 Shirtificate",  new_x="LMARGIN", new_y="NEXT", align='C')

        pdf.image("shirtificate.png", x=5, y=80, w=200) # 添加衬衫图片

        pdf.set_font("Helvetica", "B", size=25)
        pdf.set_text_color(255, 255, 255) # 将文本颜色设置为白色
        pdf.cell(0, 180, text=f"{self.name} took CS50",  new_x="LMARGIN", new_y="NEXT", align='C')

        pdf.output("shirtificate.pdf")

def main():
    Shirtificate.get_name()

if __name__ == "__main__":
    main()

