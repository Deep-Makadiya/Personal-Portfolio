"""
Generate a high-quality vector PDF resume for Deep Makadiya.
Output: assets/Deep-Makadiya-Resume.pdf
Run:    python assets/build_pdf.py
"""

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepInFrame,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT_PATH = Path(__file__).parent / "Deep-Makadiya-Resume.pdf"

NAME = "Deep Makadiya"
TITLE = "Python Developer"
EMAIL = "deepmakadia73@gmail.com"
PHONE = "+91 6353166188"
LOCATION = "Ahmedabad, India"
LINKEDIN = "linkedin.com/in/deep-makadiya-4ab258222"
GITHUB = "github.com/Deep-Makadiya"

INK = HexColor("#111111")
SUB_INK = HexColor("#333333")
RULE = HexColor("#000000")
LINK = HexColor("#0b66c3")


def build_styles():
    base = getSampleStyleSheet()
    name_style = ParagraphStyle(
        "Name",
        parent=base["Title"],
        fontName="Times-Bold",
        fontSize=24,
        leading=28,
        alignment=TA_CENTER,
        textColor=INK,
        spaceAfter=2,
    )
    title_style = ParagraphStyle(
        "Title",
        parent=base["Normal"],
        fontName="Times-Italic",
        fontSize=13,
        leading=16,
        alignment=TA_CENTER,
        textColor=SUB_INK,
        spaceAfter=8,
    )
    contact_style = ParagraphStyle(
        "Contact",
        parent=base["Normal"],
        fontName="Times-Roman",
        fontSize=10.5,
        leading=14,
        alignment=TA_CENTER,
        textColor=INK,
    )
    section_style = ParagraphStyle(
        "Section",
        parent=base["Heading2"],
        fontName="Times-Bold",
        fontSize=13,
        leading=16,
        textColor=INK,
        spaceBefore=14,
        spaceAfter=3,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=base["BodyText"],
        fontName="Times-Roman",
        fontSize=10.5,
        leading=14,
        alignment=TA_JUSTIFY,
        textColor=INK,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=body_style,
        leftIndent=12,
        bulletIndent=2,
        spaceBefore=2,
        spaceAfter=2,
    )
    role_style = ParagraphStyle(
        "Role",
        parent=base["Normal"],
        fontName="Times-Bold",
        fontSize=11.5,
        leading=14,
        textColor=INK,
    )
    company_style = ParagraphStyle(
        "Company",
        parent=base["Normal"],
        fontName="Times-Italic",
        fontSize=10.5,
        leading=13.5,
        textColor=SUB_INK,
    )
    meta_right_style = ParagraphStyle(
        "MetaRight",
        parent=base["Normal"],
        fontName="Times-Roman",
        fontSize=10.5,
        leading=13.5,
        alignment=2,
        textColor=SUB_INK,
    )
    sub_label_style = ParagraphStyle(
        "SubLabel",
        parent=base["Normal"],
        fontName="Times-Bold",
        fontSize=11,
        leading=14,
        textColor=INK,
        spaceBefore=6,
        spaceAfter=2,
    )
    return {
        "name": name_style,
        "title": title_style,
        "contact": contact_style,
        "section": section_style,
        "body": body_style,
        "bullet": bullet_style,
        "role": role_style,
        "company": company_style,
        "meta_right": meta_right_style,
        "sub_label": sub_label_style,
    }


def section_rule():
    return HRFlowable(
        width="100%", thickness=0.8, color=RULE, spaceBefore=2, spaceAfter=5
    )


def two_col_row(left_flowable, right_text, right_style, left_width=4.4, right_width=2.2):
    table = Table(
        [[left_flowable, Paragraph(right_text, right_style)]],
        colWidths=[left_width * inch, right_width * inch],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return table


def role_block(role_style, company_style, role, company):
    return [
        Paragraph(role, role_style),
        Paragraph(company, company_style),
    ]


def bullet_list(items, bullet_style):
    flow_items = [ListItem(Paragraph(text, bullet_style), leftIndent=12) for text in items]
    return ListFlowable(
        flow_items,
        bulletType="bullet",
        start="•",
        leftIndent=14,
        bulletFontName="Times-Roman",
        bulletFontSize=10.5,
        bulletColor=INK,
        spaceBefore=3,
        spaceAfter=3,
    )


def build():
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        title=f"{NAME} - Resume",
        author=NAME,
        subject="Resume",
        creator="Deep Makadiya Portfolio",
    )

    story = []

    story.append(Paragraph(NAME, styles["name"]))
    story.append(Paragraph(TITLE, styles["title"]))

    contact_line_1 = (
        f'<font color="#000000">✉ </font>'
        f'<a href="mailto:{EMAIL}"><font color="#0b66c3">{EMAIL}</font></a>'
        f'   &nbsp;<font color="#000000">☎ {PHONE}</font>'
        f'   &nbsp;<font color="#000000">⌖ {LOCATION}</font>'
    )
    contact_line_2 = (
        f'<a href="https://{LINKEDIN}"><font color="#0b66c3">{LINKEDIN}</font></a>'
        f'   &nbsp;|&nbsp;   '
        f'<a href="https://{GITHUB}"><font color="#0b66c3">{GITHUB}</font></a>'
    )
    story.append(Paragraph(contact_line_1, styles["contact"]))
    story.append(Spacer(1, 3))
    story.append(Paragraph(contact_line_2, styles["contact"]))
    story.append(Spacer(1, 6))

    story.append(Paragraph("PROFILE", styles["section"]))
    story.append(section_rule())
    profile_text = (
        "Motivated Python Developer with hands-on experience in building scalable "
        "applications, cloud solutions, and AI/ML integrations. Proficient in Python, "
        "SQL, and PostgreSQL, with a solid foundation in web technologies including "
        "HTML, CSS, and XML. Demonstrates a strong understanding of the software "
        "development lifecycle, version control practices, and database optimization "
        "techniques. Experienced in designing and deploying applications on Google "
        "Cloud Platform (GCP) and developing AI-powered solutions such as "
        "Retrieval-Augmented Generation (RAG) chatbots and Natural Language-to-SQL "
        "agents. Adept at translating complex business requirements into efficient, "
        "high-quality technical solutions, automating workflows, and delivering robust, "
        "data-driven applications."
    )
    story.append(Paragraph(profile_text, styles["body"]))

    story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["section"]))
    story.append(section_rule())

    role_left = role_block(styles["role"], styles["company"], "Python Developer", "Cravit India PVT. Ltd")
    story.append(
        two_col_row(
            role_left,
            "03/2024 – Present<br/>Ahmedabad, Gujarat, India",
            styles["meta_right"],
        )
    )
    story.append(Spacer(1, 4))

    bullets = [
        "Designed and deployed a responsive, high-performance business website with "
        "interactive UI/UX, optimized SEO, secure forms, and dynamic front-end components "
        "using HTML, CSS, JavaScript, Bootstrap, and modern web development best practices.",
        "Created a Python-based AI agent that converts natural language queries into SQL "
        "statements and returns human-readable insights, integrating with PostgreSQL/MySQL "
        "databases and using LLMs and prompt engineering techniques.",
        "Developed a Python- and Odoo-based healthcare management system to streamline "
        "dental treatment plans, appointment scheduling, billing, patient records, and "
        "automated reporting using PostgreSQL, REST APIs, HTML, and CSS.",
        "Designed and deployed a scalable serverless analytics dashboard on Google Cloud "
        "Platform with automated ETL pipelines, real-time data visualization, and "
        "IAM-based security using BigQuery, Cloud Functions, Cloud Storage, Data Studio, "
        "and Python.",
        "Developed an AI-powered intelligent support system using LLMs and RAG architecture "
        "to deliver context-aware responses with document ingestion, embedding retrieval, "
        "and NLP preprocessing using Python, LangChain, ChromaDB, and NLP techniques.",
    ]
    story.append(bullet_list(bullets, styles["bullet"]))

    story.append(Paragraph("EDUCATION", styles["section"]))
    story.append(section_rule())
    edu_left = role_block(
        styles["role"],
        styles["company"],
        "Bachelors of Engineering",
        "Apollo Institute of Engineering and Technology",
    )
    story.append(
        two_col_row(
            edu_left,
            "2020 – 2024<br/>Ahmedabad",
            styles["meta_right"],
        )
    )

    story.append(Paragraph("SKILLS", styles["section"]))
    story.append(section_rule())

    story.append(Paragraph("Programming, Frameworks &amp; Development", styles["sub_label"]))
    skills_block_1 = [
        "Python, Django, Flask, HTML, CSS, XML",
        "LLM, RAG, LangChain, Prompt Engineering",
        "Odoo Development, Odoo Framework",
        "GCP – Deployment, Environment Management &amp; Production Support",
        "Git, GitHub, Docker <i>(basic)</i>",
    ]
    story.append(bullet_list(skills_block_1, styles["bullet"]))

    story.append(Paragraph("Databases", styles["sub_label"]))
    story.append(Paragraph("PostgreSQL, SQL", styles["body"]))

    story.append(Paragraph("Business &amp; ERP Skills", styles["sub_label"]))
    skills_block_2 = [
        "Business Workflow Automation",
        "Odoo ERP Customization",
        "Report &amp; View Customization",
    ]
    story.append(bullet_list(skills_block_2, styles["bullet"]))

    frame_w = doc.width
    frame_h = doc.height
    bounded = KeepInFrame(frame_w, frame_h, story, mode="shrink")
    doc.build([bounded])
    print(f"Wrote: {OUTPUT_PATH}  ({OUTPUT_PATH.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    build()
