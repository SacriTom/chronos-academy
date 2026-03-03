"""Generate Chronos Academy Orchestration Report as PDF using fpdf2."""

from fpdf import FPDF
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "REPORT.pdf")


class ReportPDF(FPDF):
    BASALT = (28, 28, 46)
    GOLD = (197, 149, 42)
    PARCHMENT = (245, 240, 230)
    WHITE = (255, 255, 255)
    DARK_TEXT = (30, 30, 50)
    GREY = (107, 107, 123)
    LIGHT_BG = (248, 246, 241)
    BORDER_LIGHT = (224, 221, 213)

    # Agent colors
    YELLOW = (197, 149, 42)
    RED_ORANGE = (212, 114, 60)
    BLUE = (58, 107, 140)
    GREEN = (74, 124, 89)
    PURPLE = (107, 76, 138)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*self.GREY)
        self.cell(0, 6, "Chronos Academy -Multi-Agent Orchestration Report", align="L")
        self.cell(0, 6, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*self.GOLD)
        self.set_line_width(0.5)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(*self.GREY)
        self.cell(0, 10, "Octopus Multi-Agent Orchestration OS  |  CE Masters Week 7  |  March 2026", align="C")

    def section_title(self, title):
        self.ln(4)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*self.BASALT)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*self.GOLD)
        self.set_line_width(0.8)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)

    def sub_title(self, title):
        self.ln(2)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*self.BASALT)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def body_text(self, text, bold=False):
        self.set_font("Helvetica", "B" if bold else "", 10)
        self.set_text_color(*self.DARK_TEXT)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*self.DARK_TEXT)
        x = self.get_x()
        self.cell(6, 5.5, "-")
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def gold_box(self, text):
        self.set_fill_color(*self.LIGHT_BG)
        self.set_draw_color(*self.GOLD)
        self.set_line_width(0.5)
        x, y = self.get_x(), self.get_y()
        w = self.w - self.l_margin - self.r_margin
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*self.DARK_TEXT)
        self.set_xy(x + 4, y + 4)
        self.multi_cell(w - 8, 5.5, text)
        h = self.get_y() - y + 4
        self.rect(x, y, w, h, style="D")
        self.line(x, y, x, y + h)  # left accent
        self.set_draw_color(*self.GOLD)
        self.set_line_width(2.5)
        self.line(x, y, x, y + h)
        self.set_line_width(0.5)
        self.set_xy(x, y + h + 2)
        self.ln(2)

    def table(self, headers, rows, col_widths=None):
        w_avail = self.w - self.l_margin - self.r_margin
        if col_widths is None:
            col_widths = [w_avail / len(headers)] * len(headers)
        else:
            total = sum(col_widths)
            col_widths = [c / total * w_avail for c in col_widths]

        # Header
        self.set_fill_color(*self.BASALT)
        self.set_text_color(*self.PARCHMENT)
        self.set_font("Helvetica", "B", 8)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1, fill=True, align="L")
        self.ln()

        # Rows
        self.set_text_color(*self.DARK_TEXT)
        self.set_font("Helvetica", "", 8.5)
        for ri, row in enumerate(rows):
            fill = ri % 2 == 1
            if fill:
                self.set_fill_color(250, 249, 246)
            max_h = 7
            # Calculate needed height
            x_start = self.get_x()
            y_start = self.get_y()

            # First pass: measure heights
            heights = []
            for i, cell_text in enumerate(row):
                lines = self.multi_cell(col_widths[i], 5, cell_text, split_only=True)
                heights.append(max(7, len(lines) * 5))
            row_h = max(heights)

            # Check page break
            if y_start + row_h > self.h - 20:
                self.add_page()
                y_start = self.get_y()

            # Draw cells
            for i, cell_text in enumerate(row):
                x = x_start + sum(col_widths[:i])
                self.set_xy(x, y_start)
                if fill:
                    self.rect(x, y_start, col_widths[i], row_h, style="F")
                self.set_draw_color(*self.BORDER_LIGHT)
                self.rect(x, y_start, col_widths[i], row_h, style="D")
                self.set_xy(x + 1, y_start + 1)
                self.multi_cell(col_widths[i] - 2, 5, cell_text)

            self.set_xy(x_start, y_start + row_h)
        self.ln(4)

    def agent_badge(self, x, y, w, h, label, sublabel, color):
        self.set_fill_color(*color)
        self.set_draw_color(*color)
        self.rect(x, y, w, h, style="F", round_corners=True, corner_radius=3)
        self.set_xy(x, y + 3)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*self.WHITE)
        self.cell(w, 6, label, align="C")
        self.set_xy(x, y + 10)
        self.set_font("Helvetica", "", 7)
        self.cell(w, 5, sublabel, align="C")

    def step_badge(self, text, color):
        self.set_font("Helvetica", "B", 7.5)
        tw = self.get_string_width(text) + 8
        x, y = self.get_x(), self.get_y()
        self.set_fill_color(*color)
        self.rect(x, y, tw, 5.5, style="F")
        self.set_text_color(*self.WHITE)
        self.set_xy(x, y)
        self.cell(tw, 5.5, text, align="C")
        self.cell(3, 5.5, "")

    def metric_box(self, x, y, value, label):
        w, h = 55, 35
        self.set_fill_color(*self.LIGHT_BG)
        self.set_draw_color(*self.BORDER_LIGHT)
        self.rect(x, y, w, h, style="DF", round_corners=True, corner_radius=4)
        self.set_xy(x, y + 4)
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(*self.GOLD)
        self.cell(w, 10, str(value), align="C")
        self.set_xy(x, y + 17)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*self.GREY)
        self.cell(w, 5, label.upper(), align="C")


def build_pdf():
    pdf = ReportPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(18, 15, 18)

    # ==================== COVER PAGE ====================
    pdf.add_page()
    pdf.set_fill_color(*ReportPDF.BASALT)
    pdf.rect(0, 0, 210, 297, style="F")

    # Logo circle
    pdf.set_draw_color(*ReportPDF.GOLD)
    pdf.set_line_width(1)
    pdf.circle(105, 80, 20, style="D")
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.set_xy(0, 70)
    pdf.cell(210, 20, "CA", align="C")

    # Title
    pdf.set_font("Helvetica", "B", 32)
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.set_xy(0, 110)
    pdf.cell(210, 14, "CHRONOS ACADEMY", align="C")

    # Subtitle
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(*ReportPDF.PARCHMENT)
    pdf.set_xy(0, 128)
    pdf.cell(210, 8, "Multi-Agent Orchestration Report", align="C")

    # Divider
    pdf.set_draw_color(*ReportPDF.GOLD)
    pdf.set_line_width(0.5)
    pdf.line(75, 145, 135, 145)

    # Meta info
    meta = [
        ("Course", "Customer Engagement -CE Masters, Week 7"),
        ("Date", "3 March 2026"),
        ("Framework", "Octopus Multi-Agent Orchestration OS"),
        ("Author", "SacriTom"),
    ]
    y = 155
    for label, value in meta:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*ReportPDF.PARCHMENT)
        pdf.set_xy(50, y)
        pdf.cell(35, 6, label + ":", align="R")
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(209, 207, 199)
        pdf.cell(80, 6, value)
        y += 8

    # URL box
    pdf.set_draw_color(*ReportPDF.GOLD)
    pdf.set_line_width(0.8)
    url_text = "sacritom.github.io/chronos-academy"
    pdf.set_font("Courier", "B", 11)
    tw = pdf.get_string_width(url_text) + 20
    pdf.set_xy((210 - tw) / 2, 205)
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.cell(tw, 12, url_text, border=1, align="C")

    # Motto
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(*ReportPDF.GREY)
    pdf.set_xy(0, 235)
    pdf.cell(210, 6, '"Tempus docet. Nos discimus." -Time teaches. We learn.', align="C")

    # ==================== PAGE 2: EXECUTIVE SUMMARY ====================
    pdf.add_page()

    pdf.section_title("1. Executive Summary")
    pdf.gold_box(
        'This report documents the end-to-end process of building "Chronos Academy" -a fictitious '
        "time-travel university -using Octopus, a multi-agent orchestration framework. Five specialist "
        "AI agents (Researcher, Designer, Maker, Marketer) were coordinated by a Purple Manager agent "
        "to deliver a complete creative product: from worldbuilding through website deployment -in "
        "under 30 minutes.\n\n"
        "The project demonstrates three orchestration patterns: parallel fan-out (independent tasks "
        "running simultaneously), sequential pipeline (dependent phases in order), and manager-direct "
        "execution (coordination tasks handled by the orchestrator). The final deliverable is a live, "
        "responsive single-page website deployed to GitHub Pages."
    )

    # ==================== AGENT ROSTER ====================
    pdf.section_title("2. Agent Roster")
    pdf.body_text(
        "Octopus defines five specialist agent roles. Each operates under a contract "
        "specifying its scope, output format, and escalation rules:"
    )

    badge_y = pdf.get_y() + 2
    agents = [
        ("Researcher", "Intelligence", ReportPDF.YELLOW),
        ("Designer", "Architecture", ReportPDF.RED_ORANGE),
        ("Maker", "Building", ReportPDF.BLUE),
        ("Marketer", "Growth", ReportPDF.GREEN),
        ("Manager", "Orchestration", ReportPDF.PURPLE),
    ]
    bw = 32
    gap = 3
    start_x = (210 - (bw * 5 + gap * 4)) / 2
    for i, (name, role, color) in enumerate(agents):
        pdf.agent_badge(start_x + i * (bw + gap), badge_y, bw, 20, name, role, color)
    pdf.set_xy(18, badge_y + 28)

    # ==================== TIMELINE ====================
    pdf.section_title("3. Orchestration Timeline")

    # Step 0
    pdf.sub_title("Step 0: Project Setup  (T+0 min)")
    pdf.step_badge("Purple Manager", ReportPDF.PURPLE)
    pdf.step_badge("Setup", (140, 140, 155))
    pdf.ln(4)
    pdf.bullet("Cloned the Octopus orchestration framework from GitHub")
    pdf.bullet("Created a private copy on personal GitHub (SacriTom/octopus)")
    pdf.bullet('Selected project concept: "Chronos Academy" (time-travel university)')
    pdf.bullet("Created project folder with tracking documents: PROJECT_STATE.md, CHANGELOG.md, QUICKSTART.md")
    pdf.body_text("Output: Project scaffold with 4-phase plan", bold=True)

    # Step 1
    pdf.sub_title("Step 1: Research & Worldbuilding  (T+5 min)")
    pdf.step_badge("Yellow Researcher x5", ReportPDF.YELLOW)
    pdf.step_badge("Parallel Fan-Out", (58, 107, 140))
    pdf.step_badge("~4 min", (74, 124, 89))
    pdf.ln(4)
    pdf.body_text("Five independent research briefs dispatched simultaneously:")
    pdf.table(
        ["#", "Brief", "Output File", "Key Deliverables"],
        [
            ["1", "Origin Story & Charter", "research/01-origin-story.md", "Founding lore, Dr. Elara Voss, the Meridian, 7 charter principles"],
            ["2", "Eras & Campuses", "research/02-eras-and-campuses.md", "8 era-campuses spanning 68M BCE to 22nd century"],
            ["3", "Faculty Roster", "research/03-faculty-roster.md", "16 historical figures as professors, 6 departments"],
            ["4", "Course Catalog", "research/04-course-catalog.md", "22 courses, 4 degree programs, academic calendar"],
            ["5", "Student Life", "research/05-student-life.md", "Housing, 9 clubs, traditions, temporal ethics"],
        ],
        col_widths=[8, 28, 42, 70],
    )
    pdf.body_text("Why parallel: All five tasks were independent -no agent needed another's output. This is the textbook case for fan-out orchestration.")

    # Step 2
    pdf.sub_title("Step 2: Design  (T+10 min)")
    pdf.step_badge("Red-Orange Designer x4", ReportPDF.RED_ORANGE)
    pdf.step_badge("Parallel Fan-Out", (58, 107, 140))
    pdf.step_badge("~4 min", (74, 124, 89))
    pdf.ln(4)
    pdf.body_text("Four design briefs dispatched simultaneously, each receiving the research output:")
    pdf.table(
        ["#", "Brief", "Output File", "Key Deliverables"],
        [
            ["1", "Brand Identity", "design/01-brand-identity.md", "Logo concept, color palette, typography, CSS custom properties"],
            ["2", "Site Map & IA", "design/02-site-map.md", "Single-page MVP layout (8 sections), content priority matrix"],
            ["3", "Wireframes", "design/03-wireframes.md", "ASCII wireframes for all 8 sections, responsive specs"],
            ["4", "Campus Visuals", "design/04-campus-visuals.md", "Per-campus color schemes, CSS gradients, card specs"],
        ],
        col_widths=[8, 25, 42, 70],
    )
    pdf.body_text("Quality gate: All four docs delivered consistent specs. CSS variables from doc 01 were directly consumable by the build phase.")

    # Step 3
    pdf.sub_title("Step 3: Build  (T+15 min)")
    pdf.step_badge("Blue Maker x1", ReportPDF.BLUE)
    pdf.step_badge("Sequential Pipeline", (58, 107, 140))
    pdf.step_badge("~6 min", (74, 124, 89))
    pdf.ln(4)
    pdf.body_text("Input: 5 research docs + 4 design docs (9 files total)", bold=True)
    pdf.body_text("Output: build/index.html -1,978 lines, 65KB, single self-contained HTML", bold=True)
    pdf.bullet("8-section single-page scrolling website with all content from research")
    pdf.bullet("Dark mode default (Deep Basalt #1C1C2E) with Meridian Gold accents")
    pdf.bullet("8 campus cards with era-specific accent colors, 16 faculty cards with real quotes")
    pdf.bullet("4 degree program cards, student life highlights, cinematic Temporal Oath section")
    pdf.bullet("Sticky nav, mobile hamburger menu, scroll-triggered fade-in animations")
    pdf.bullet("Fully responsive (desktop, tablet, mobile)")
    pdf.body_text("Why sequential: The build required complete research AND design specs -a strict dependency chain.")

    # Step 4
    pdf.sub_title("Step 4: Deployment  (T+22 min)")
    pdf.step_badge("Purple Manager", ReportPDF.PURPLE)
    pdf.step_badge("Manager Direct", (140, 140, 155))
    pdf.step_badge("~3 min", (74, 124, 89))
    pdf.ln(4)
    pdf.bullet("Created GitHub repository: SacriTom/chronos-academy")
    pdf.bullet("Pushed all project files (research, design, build, tracking docs)")
    pdf.bullet("Enabled GitHub Pages on master branch")
    pdf.bullet("Verified live deployment")
    pdf.body_text("Live URL: https://sacritom.github.io/chronos-academy/", bold=True)

    # ==================== FLOW DIAGRAM ====================
    # Only add page if not enough room for the diagram (135mm needed)
    if pdf.get_y() > 140:
        pdf.add_page()
    pdf.section_title("4. Orchestration Flow")

    # Dark background box
    box_x, box_y = 18, pdf.get_y()
    box_w, box_h = 174, 135
    pdf.set_fill_color(*ReportPDF.BASALT)
    pdf.rect(box_x, box_y, box_w, box_h, style="F", round_corners=True, corner_radius=4)

    # Title
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.set_xy(box_x, box_y + 5)
    pdf.cell(box_w, 7, "Multi-Agent Orchestration Pipeline", align="C")

    # Manager
    cx = box_x + box_w / 2
    pdf.set_fill_color(*ReportPDF.PURPLE)
    mw, mh = 50, 10
    pdf.rect(cx - mw/2, box_y + 16, mw, mh, style="F", round_corners=True, corner_radius=3)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*ReportPDF.WHITE)
    pdf.set_xy(cx - mw/2, box_y + 18)
    pdf.cell(mw, 6, "PURPLE MANAGER", align="C")

    # Arrow
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_xy(cx - 5, box_y + 26)
    pdf.cell(10, 5, "|", align="C")

    # Phase 1 label
    pdf.set_font("Helvetica", "", 6)
    pdf.set_text_color(150, 150, 165)
    pdf.set_xy(box_x, box_y + 32)
    pdf.cell(box_w, 4, "PHASE 1: RESEARCH -Parallel Fan-Out", align="C")

    # Y boxes
    yw = 16
    ygap = 3
    y_row_y = box_y + 37
    y_start = cx - (5 * yw + 4 * ygap) / 2
    for i in range(5):
        pdf.set_fill_color(*ReportPDF.YELLOW)
        bx = y_start + i * (yw + ygap)
        pdf.rect(bx, y_row_y, yw, 9, style="F", round_corners=True, corner_radius=2)
        pdf.set_font("Helvetica", "B", 7)
        pdf.set_text_color(*ReportPDF.BASALT)
        pdf.set_xy(bx, y_row_y + 2)
        pdf.cell(yw, 5, f"Y{i+1}", align="C")

    # Arrow
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_xy(cx - 5, y_row_y + 10)
    pdf.cell(10, 5, "|", align="C")

    # Phase 2 label
    pdf.set_font("Helvetica", "", 6)
    pdf.set_text_color(150, 150, 165)
    pdf.set_xy(box_x, y_row_y + 16)
    pdf.cell(box_w, 4, "PHASE 2: DESIGN -Parallel Fan-Out", align="C")

    # D boxes
    d_row_y = y_row_y + 21
    d_start = cx - (4 * yw + 3 * ygap) / 2
    for i in range(4):
        pdf.set_fill_color(*ReportPDF.RED_ORANGE)
        bx = d_start + i * (yw + ygap)
        pdf.rect(bx, d_row_y, yw, 9, style="F", round_corners=True, corner_radius=2)
        pdf.set_font("Helvetica", "B", 7)
        pdf.set_text_color(*ReportPDF.WHITE)
        pdf.set_xy(bx, d_row_y + 2)
        pdf.cell(yw, 5, f"D{i+1}", align="C")

    # Arrow
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_xy(cx - 5, d_row_y + 10)
    pdf.cell(10, 5, "|", align="C")

    # Quality Gate
    gate_y = d_row_y + 16
    gw = 40
    pdf.set_draw_color(*ReportPDF.GOLD)
    pdf.set_line_width(0.6)
    pdf.rect(cx - gw/2, gate_y, gw, 9, style="D", round_corners=True, corner_radius=3)
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.set_xy(cx - gw/2, gate_y + 2)
    pdf.cell(gw, 5, "QUALITY GATE", align="C")

    # Arrow
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_xy(cx - 5, gate_y + 10)
    pdf.cell(10, 5, "|", align="C")

    # Build
    build_y = gate_y + 16
    pdf.set_fill_color(*ReportPDF.BLUE)
    bw2 = 40
    pdf.rect(cx - bw2/2, build_y, bw2, 9, style="F", round_corners=True, corner_radius=3)
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_text_color(*ReportPDF.WHITE)
    pdf.set_xy(cx - bw2/2, build_y + 2)
    pdf.cell(bw2, 5, "BLUE MAKER", align="C")

    # Arrow
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_xy(cx - 5, build_y + 10)
    pdf.cell(10, 5, "|", align="C")

    # Deploy
    dep_y = build_y + 16
    pdf.set_fill_color(*ReportPDF.GREEN)
    pdf.rect(cx - bw2/2, dep_y, bw2, 9, style="F", round_corners=True, corner_radius=3)
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_text_color(*ReportPDF.WHITE)
    pdf.set_xy(cx - bw2/2, dep_y + 2)
    pdf.cell(bw2, 5, "LIVE SITE", align="C")

    # Legend
    pdf.set_font("Helvetica", "", 6)
    pdf.set_text_color(150, 150, 165)
    pdf.set_xy(box_x, box_y + box_h - 8)
    pdf.cell(box_w, 5, "Y = Yellow Researcher    D = Red-Orange Designer    Blue = Maker    Purple = Manager", align="C")

    pdf.set_xy(18, box_y + box_h + 6)

    # ==================== PATTERNS ====================
    pdf.section_title("5. Orchestration Patterns Used")
    pdf.table(
        ["Pattern", "Phase", "Description"],
        [
            ["Parallel Fan-Out", "Phase 1 (Research)", "5 independent researcher agents dispatched simultaneously"],
            ["Parallel Fan-Out", "Phase 2 (Design)", "4 independent designer agents dispatched simultaneously"],
            ["Sequential Pipeline", "Phase 2 > 3", "Research feeds Design feeds Build -each depends on previous"],
            ["Single Agent", "Phase 3 (Build)", "One Maker agent consumed all 9 input docs, built the site"],
            ["Manager Direct", "Phase 4 (Deploy)", "Purple Manager handled deployment directly"],
        ],
        col_widths=[30, 25, 90],
    )

    # ==================== METRICS ====================
    # Ensure metrics fit on one page
    if pdf.get_y() > 180:
        pdf.add_page()
    pdf.section_title("6. Project Metrics")

    my = pdf.get_y() + 2
    metrics = [
        ("10", "Agents Spawned"),
        ("2", "Parallel Batches"),
        ("3", "Sequential Handoffs"),
        ("14", "Files Created"),
        ("65KB", "Site Size"),
        ("~25m", "Elapsed Time"),
    ]
    mw_box = 55
    mgap = 3
    row_w = 3 * mw_box + 2 * mgap
    mx_start = (210 - row_w) / 2
    for i, (val, label) in enumerate(metrics):
        row = i // 3
        col = i % 3
        pdf.metric_box(mx_start + col * (mw_box + mgap), my + row * 40, val, label)

    pdf.set_xy(18, my + 85)

    # ==================== OBSERVATIONS ====================
    pdf.section_title("7. Key Observations")

    pdf.sub_title("What Worked Well")
    successes = [
        ("Parallel fan-out reduced elapsed time", "5 research briefs in ~4 min, 4 design docs in ~4 min (vs ~15 and ~12 min sequentially). A 3x speedup."),
        ("Clear spawn templates", "Each agent received TASK, OUTPUT, FORMAT, SCOPE, and ESCALATE rules from the Octopus framework."),
        ("Scoped autonomy", "Agents stayed in their lane: researchers didn't design, designers didn't build. Scope boundaries prevented drift."),
        ("Design tokens bridged phases", "Brand identity CSS custom properties were consumed directly by the Maker. Zero translation loss between phases."),
    ]
    for title, desc in successes:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*ReportPDF.GREEN)
        pdf.cell(3, 5, ">")
        pdf.set_text_color(*ReportPDF.DARK_TEXT)
        pdf.cell(0, 5, title, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*ReportPDF.GREY)
        pdf.set_x(22)
        pdf.multi_cell(0, 4.5, desc)
        pdf.ln(2)

    pdf.sub_title("Challenges & Lessons")
    challenges = [
        ("Cross-reference consistency", "Parallel agents can't coordinate, so faculty/campus details varied slightly. The Maker reconciled during build."),
        ("Context window pressure", "The Maker needed 9 documents (~100K tokens) as input. Required single-agent sequential over parallel."),
        ("GitHub Pages path limitation", "Pages only serves from / or /docs, not /build. Required an extra copy step during deployment."),
        ("The Manager principle holds", '"If you\'re doing the work, you\'re not managing." Purple orchestrated 10 agents and only executed deployment directly.'),
    ]
    for title, desc in challenges:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*ReportPDF.RED_ORANGE)
        pdf.cell(3, 5, ">")
        pdf.set_text_color(*ReportPDF.DARK_TEXT)
        pdf.cell(0, 5, title, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*ReportPDF.GREY)
        pdf.set_x(22)
        pdf.multi_cell(0, 4.5, desc)
        pdf.ln(2)

    # ==================== FILE INVENTORY ====================
    pdf.add_page()
    pdf.section_title("8. File Inventory")
    pdf.table(
        ["File", "Purpose", "Phase", "Agent"],
        [
            ["PROJECT_STATE.md", "Plan & progress tracking", "Setup", "Purple Manager"],
            ["CHANGELOG.md", "Version-controlled change log", "Setup", "Purple Manager"],
            ["QUICKSTART.md", "Session resume prompt", "Setup", "Purple Manager"],
            ["REPORT.md", "Orchestration report", "All", "Purple Manager"],
            ["research/01-origin-story.md", "Founding lore & charter", "Research", "Yellow Researcher"],
            ["research/02-eras-and-campuses.md", "8 era-campuses", "Research", "Yellow Researcher"],
            ["research/03-faculty-roster.md", "16-professor faculty", "Research", "Yellow Researcher"],
            ["research/04-course-catalog.md", "22 courses, 4 degrees", "Research", "Yellow Researcher"],
            ["research/05-student-life.md", "Student life & culture", "Research", "Yellow Researcher"],
            ["design/01-brand-identity.md", "Brand system & CSS tokens", "Design", "Red-Orange Designer"],
            ["design/02-site-map.md", "Site architecture & IA", "Design", "Red-Orange Designer"],
            ["design/03-wireframes.md", "Section wireframes", "Design", "Red-Orange Designer"],
            ["design/04-campus-visuals.md", "Campus visual specs", "Design", "Red-Orange Designer"],
            ["build/index.html", "Complete website (65KB)", "Build", "Blue Maker"],
            ["index.html", "GitHub Pages deploy copy", "Deploy", "Purple Manager"],
        ],
        col_widths=[45, 30, 15, 28],
    )

    # ==================== CONCLUSION ====================
    pdf.ln(4)
    # Dark conclusion box
    conc_y = pdf.get_y()
    conc_h = 60
    pdf.set_fill_color(*ReportPDF.BASALT)
    pdf.rect(18, conc_y, 174, conc_h, style="F", round_corners=True, corner_radius=4)

    pdf.set_xy(24, conc_y + 6)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.cell(162, 8, "9. Conclusion")
    pdf.set_draw_color(*ReportPDF.GOLD)
    pdf.set_line_width(0.5)
    pdf.line(24, conc_y + 15, 186, conc_y + 15)

    pdf.set_xy(24, conc_y + 19)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(209, 207, 199)
    pdf.multi_cell(162, 5,
        "This project demonstrated multi-agent orchestration using the Octopus framework "
        "to build a complete creative product -from zero to a live, deployed website -in "
        "under 30 minutes. The key orchestration insight: use parallel fan-out for independent "
        "work, sequential pipelines for dependent work, and keep the Manager focused on "
        "coordination, not execution."
    )

    pdf.set_xy(24, conc_y + 42)
    pdf.set_font("Courier", "B", 10)
    pdf.set_text_color(*ReportPDF.GOLD)
    pdf.cell(162, 6, "https://sacritom.github.io/chronos-academy/", align="C")

    pdf.set_xy(24, conc_y + 51)
    pdf.set_font("Helvetica", "I", 7)
    pdf.set_text_color(*ReportPDF.GREY)
    pdf.cell(162, 5, "Octopus Multi-Agent Orchestration OS  |  CE Masters Week 7  |  March 2026", align="C")

    # ==================== SAVE ====================
    pdf.output(OUTPUT_PATH)
    print(f"PDF saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
