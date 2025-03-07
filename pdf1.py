# imports module
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
    [ "Date" , "Name", "Subscription", "Price (Rs.)" ],
    [
        "16/11/2020",
        "Full Stack Development  - Live",
        "Lifetime",
        "10,99.00/-",
    ],
    [ "16/11/2020", "Yuvraj Classes: Live", "8 Months", "9,999.00/-"],
    [ "Sub Total", "", "", "208.00/-"],
    [ "Discount", "", "", "-30.00/-"],
    [ "Total", "", "", "178.00/-"],
]

pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )

styles = getSampleStyleSheet()

title_style = styles[ "Heading1" ]

title_style.alignment = 1

title = Paragraph( "Codewithrandom" , title_style )


style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
    ]
)

table = Table( DATA , style = style )

pdf.build([ title , table ])
