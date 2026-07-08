"""
========================================================================
Project Name: F1 Nexus
Developer: Renad Kafyah
Framework: KivyMD / Kivy
========================================================================
"""

import os
# Force landscape orientation for immersive simulator experience
os.environ['KIVY_ORIENTATION'] = 'LandscapeLeft LandscapeRight'

from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    MainMenuScreen:
    RaceCenterScreen:
    SimulationScreen:
    AnalyticsScreen:

# ---- SCREEN 1: MODERN COCKPIT MAIN MENU ----
<MainMenuScreen>:
    name: 'main_menu'
    MDFloatLayout:
        # Dark Cyber-Asphalt Premium Gradient Background
        canvas.before:
            Color:
                rgba: 0.04, 0.04, 0.06, 1
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: 0.12, 0.02, 0.02, 0.4  # Dynamic Red Glow from the right
            Quad:
                points: [self.width*0.5, 0,  self.width, 0,  self.width, self.height,  self.width*0.7, self.height]

        # Decorative Racing Stripe Background
        MDFloatLayout:
            size_hint: (1, 1)
            canvas.before:
                Color:
                    rgba: 0.9, 0.1, 0.1, 0.03
                Line:
                    points: [0, self.height*0.15, self.width, self.height*0.15]
                    width: 2

        # Brand Identity Header with Custom Icon
        MDBoxLayout:
            orientation: 'horizontal'
            pos_hint: {"x": 0.05, "top": 0.95}
            size_hint: (0.4, 0.1)
            spacing: 10
            
            MDIcon:
                icon: "racing-helmet"
                theme_text_color: "Custom"
                text_color: 0.9, 0.1, 0.1, 1
                font_size: "36sp"
                pos_hint: {"center_y": 0.5}

            MDLabel:
                text: "F1 NEXUS"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "H4"
                bold: True
                pos_hint: {"center_y": 0.5}

        # Premium Status Hub (Telemetry & Status Indicators)
        MDCard:
            size_hint: (0.42, 0.08)
            pos_hint: {"right": 0.95, "top": 0.93}
            md_bg_color: 0.08, 0.08, 0.12, 0.9
            radius: [12,]
            padding: [15, 0, 15, 0]
            ripple_behavior: True
            elevation: 2
            
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: 15
                MDLabel:
                    text: "🪙 12,450"
                    halign: "center"
                    bold: True
                    text_color: 1, 0.8, 0.2, 1
                    theme_text_color: "Custom"
                MDLabel:
                    text: "⚡ AI ENGAGED"
                    halign: "center"
                    bold: True
                    text_color: 0.2, 0.8, 0.2, 1
                    theme_text_color: "Custom"
                MDLabel:
                    text: "🏆 LIVE PODIUM"
                    halign: "center"
                    bold: True
                    text_color: 0.2, 0.6, 1, 1
                    theme_text_color: "Custom"

        # Main Interactive Hub & Hero Section (Left-Aligned)
        MDCard:
            size_hint: (0.52, 0.52)
            pos_hint: {"x": 0.05, "center_y": 0.48}
            md_bg_color: 0.06, 0.06, 0.09, 0.75
            radius: [16,]
            padding: 25
            orientation: 'vertical'
            spacing: 15
            line_color: [0.9, 0.1, 0.1, 0.15]

            MDLabel:
                text: "RACE STRATEGY COMMAND"
                theme_text_color: "Custom"
                text_color: 0.9, 0.1, 0.1, 1
                font_style: "H5"
                bold: True

            MDLabel:
                text: "Simulate live racing vectors, analyze real-time tyre telemetry, and optimize your pit strategy utilizing our predictive deep learning engine."
                theme_text_color: "Custom"
                text_color: 0.85, 0.85, 0.9, 1
                font_style: "Body1"
                line_height: 1.2

            MDRaisedButton:
                text: "🏁 START LIVE SESSION OVERVIEW"
                size_hint: (1, 0.3)
                md_bg_color: 0.9, 0.1, 0.1, 1
                elevation: 4
                font_style: "Button"
                on_release: root.manager.current = 'race_center'

        # Right Decorative Preview Card (Simulating Live Track View)
        MDCard:
            size_hint: (0.33, 0.52)
            pos_hint: {"right": 0.95, "center_y": 0.48}
            md_bg_color: 0.06, 0.06, 0.09, 0.75
            radius: [16,]
            padding: 20
            orientation: 'vertical'
            spacing: 10
            line_color: [1, 1, 1, 0.05]

            MDLabel:
                text: "LIVE TRACK FEED"
                font_style: "Subtitle2"
                bold: True
                text_color: 0.6, 0.6, 0.65, 1
            
            # Local Image fallback with dark neon style placeholder if image fails
            MDFloatLayout:
                canvas.before:
                    Color:
                        rgba: 0.03, 0.03, 0.05, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                Image:
                    source: 'f1_bg.png'
                    allow_stretch: True
                    keep_ratio: False
                    size_hint: (1, 1)
                    pos_hint: {"x": 0, "y": 0}
                MDLabel:
                    text: "[ NO VIDEO FEED ]\\nAI Telemetry Active"
                    halign: "center"
                    valign: "middle"
                    font_style: "Caption"
                    text_color: 0.9, 0.1, 0.1, 0.6
                    bold: True

        # Sleek Bottom Professional Navigation Matrix
        MDCard:
            size_hint: (0.9, 0.14)
            pos_hint: {"center_x": 0.5, "y": 0.06}
            md_bg_color: 0.06, 0.06, 0.09, 0.9
            radius: [16,]
            padding: [15, 0, 15, 0]
            elevation: 3
            line_color: [1, 1, 1, 0.03]
            
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: 12
                
                MDFillRoundFlatIconButton:
                    icon: "view-dashboard"
                    text: "CORE DASHBOARD"
                    md_bg_color: 0.9, 0.1, 0.1, 1
                    size_hint_y: 0.6
                    pos_hint: {"center_y": 0.5}
                MDFlatButton:
                    text: "📊 TELEMETRY FEED"
                    text_color: 1, 1, 1, 1
                    size_hint_y: 0.6
                    pos_hint: {"center_y": 0.5}
                    on_release: root.manager.current = 'race_center'
                MDFlatButton:
                    text: "⚙️ WHAT-IF SIM"
                    text_color: 1, 1, 1, 1
                    size_hint_y: 0.6
                    pos_hint: {"center_y": 0.5}
                    on_release: root.manager.current = 'simulation'
                MDFlatButton:
                    text: "🔮 AI FORECASTS"
                    text_color: 1, 1, 1, 1
                    size_hint_y: 0.6
                    pos_hint: {"center_y": 0.5}
                    on_release: root.manager.current = 'analytics'


# ---- SCREEN 2: TELEMETRY ANALYSIS ----
<RaceCenterScreen>:
    name: 'race_center'
    MDFloatLayout:
        md_bg_color: 0.04, 0.04, 0.06, 1

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"x": 0.03, "top": 0.97}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: root.manager.current = 'main_menu'

        MDLabel:
            text: "📊 LIVE TRACK TELEMETRY // REAL-TIME METRICS"
            pos_hint: {"center_x": 0.5, "top": 0.95}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "H6"
            bold: True

        MDCard:
            size_hint: (0.49, 0.7)
            pos_hint: {"x": 0.04, "y": 0.1}
            md_bg_color: 0.06, 0.06, 0.09, 1
            radius: [14,]
            padding: 20
            orientation: 'vertical'
            spacing: 12

            MDLabel:
                text: "🏎️ PERFORMANCE MATRIX (LAP 42/57)"
                bold: True
                text_color: 0.9, 0.1, 0.1, 1
            
            MDLabel:
                text: "SPEED: ████████████████ 328 km/h"
                text_color: 0.2, 0.9, 0.2, 1
                font_style: "Button"
            MDLabel:
                text: "THROTTLE: ████████████░░░░ 82%"
                text_color: 1, 1, 1, 1
                font_style: "Caption"
            MDLabel:
                text: "DRS STATUS: ACTIVE 🟢"
                text_color: 0.2, 0.9, 0.2, 1
                font_style: "Caption"
            MDLabel:
                text: "ENGINE TEMP: 112°C | ERS STRATEGY: OPTIMAL"
                text_color: 0.9, 0.6, 0.1, 1
                font_style: "Caption"

        MDCard:
            size_hint: (0.39, 0.7)
            pos_hint: {"right": 0.96, "y": 0.1}
            md_bg_color: 0.06, 0.06, 0.09, 1
            radius: [14,]
            padding: 20
            orientation: 'vertical'
            spacing: 15

            MDLabel:
                text: "🛞 TYRE DEGRADATION ANALYSIS"
                bold: True
                halign: "center"
                text_color: 1, 1, 1, 1

            MDBoxLayout:
                orientation: 'horizontal'
                spacing: 10
                MDLabel:
                    text: "🔴 FRONT L\\n Wear: 68%\\n Temp: 98°C"
                    halign: "center"
                    font_style: "Caption"
                MDLabel:
                    text: "🔴 FRONT R\\n Wear: 64%\\n Temp: 95°C"
                    halign: "center"
                    font_style: "Caption"
            
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: 10
                MDLabel:
                    text: "🟢 REAR L\\n Wear: 42%\\n Temp: 102°C"
                    halign: "center"
                    font_style: "Caption"
                MDLabel:
                    text: "🟢 REAR R\\n Wear: 40%\\n Temp: 101°C"
                    halign: "center"
                    font_style: "Caption"

            MDRaisedButton:
                text: "RUN SIMULATION GENERATOR ➡️"
                size_hint_x: 1
                md_bg_color: 0.9, 0.1, 0.1, 1
                on_release: root.manager.current = 'simulation'


# ---- SCREEN 3: STRATEGIC SIMULATOR ----
<SimulationScreen>:
    name: 'simulation'
    MDFloatLayout:
        md_bg_color: 0.04, 0.04, 0.06, 1

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"x": 0.03, "top": 0.97}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: root.manager.current = 'main_menu'

        MDLabel:
            text: "⚙️ AI predictive WHAT-IF SIMULATOR"
            pos_hint: {"center_x": 0.5, "top": 0.95}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "H6"
            bold: True

        MDCard:
            size_hint: (0.46, 0.7)
            pos_hint: {"x": 0.04, "y": 0.1}
            md_bg_color: 0.06, 0.06, 0.09, 1
            radius: [14,]
            padding: 20
            orientation: 'vertical'
            spacing: 12
            
            MDLabel:
                text: "📊 PREDICTIVE RUNS COMPARISON"
                bold: True
                font_style: "Subtitle1"
                text_color: 1, 1, 1, 1
            
            MDBoxLayout:
                orientation: 'vertical'
                spacing: 8
                MDLabel:
                    text: "Lap 45: [ 🟥🟥🟥🟥🟥🟥🟥🟥🟩🟩 ] +2.4s"
                    font_style: "Caption"
                MDLabel:
                    text: "Lap 50: [ 🟥🟥🟥🟥🟥🟥🟩🟩🟩🟩 ] +4.1s"
                    font_style: "Caption"
                MDLabel:
                    text: "Lap 55: [ 🟥🟥🟥🟥🟩🟩🟩🟩🟩🟩 ] P1 ESTIMATED WIN"
                    font_style: "Caption"
                    bold: True
                    text_color: 0.2, 0.9, 0.2, 1
                
            MDLabel:
                text: "Simulations indicate that Strategy B (Defensive One-Stop) safely bypasses mid-field traffic delays with optimal efficiency indexes."
                font_style: "Body2"
                theme_text_color: "Secondary"

        MDBoxLayout:
            orientation: 'vertical'
            size_hint: (0.42, 0.7)
            pos_hint: {"right": 0.96, "y": 0.1}
            spacing: 15

            MDCard:
                md_bg_color: 0.08, 0.08, 0.12, 1
                radius: [12,]
                padding: 15
                orientation: 'horizontal'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        text: "⚔️ MODE A: ULTRA ATTACK"
                        bold: True
                        text_color: 0.9, 0.1, 0.1, 1
                    MDLabel:
                        text: "Immediate Box for Softs. High traffic risk."
                        font_style: "Caption"
                MDRaisedButton:
                    text: "RUN"
                    md_bg_color: 0.2, 0.2, 0.28, 1

            MDCard:
                md_bg_color: 0.08, 0.08, 0.12, 1
                radius: [12,]
                padding: 15
                orientation: 'horizontal'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        text: "🛡️ MODE B: EXTEND & OVERCUT"
                        bold: True
                        text_color: 0.2, 0.8, 0.2, 1
                    MDLabel:
                        text: "Delay Pit Stop 4 laps. Gain clean track."
                        font_style: "Caption"
                MDRaisedButton:
                    text: "DEPLOY"
                    md_bg_color: 0.9, 0.1, 0.1, 1
                    on_release: root.manager.current = 'analytics'


# ---- SCREEN 4: AI FORECAST ADVANCED ----
<AnalyticsScreen>:
    name: 'analytics'
    MDFloatLayout:
        md_bg_color: 0.04, 0.04, 0.06, 1

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"x": 0.03, "top": 0.97}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: root.manager.current = 'main_menu'

        MDLabel:
            text: "🔮 ADVANCED MODEL METRICS // DEEP LEARNING"
            pos_hint: {"center_x": 0.5, "top": 0.95}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "H6"
            bold: True

        MDCard:
            size_hint: (0.44, 0.7)
            pos_hint: {"x": 0.04, "y": 0.1}
            md_bg_color: 0.06, 0.06, 0.09, 1
            radius: [14,]
            padding: 20
            orientation: 'vertical'
            spacing: 15
            
            MDLabel:
                text: "🌧️ METEOROLOGICAL LIVE RADAR"
                bold: True
                text_color: 0.1, 0.6, 0.9, 1
            
            MDCard:
                md_bg_color: 0.08, 0.08, 0.14, 1
                radius: [10,]
                padding: 15
                MDLabel:
                    text: "🌦️ PRECIPITATION RISK TIMELINE:\\n• Laps 43-46: 15% (Dry)\\n• Laps 47-52: 85% (Wet Peak Horizon)"
                    halign: "center"
                    bold: True
                    font_style: "Body2"

        MDCard:
            size_hint: (0.44, 0.7)
            pos_hint: {"right": 0.96, "y": 0.1}
            md_bg_color: 0.06, 0.06, 0.09, 1
            radius: [14,]
            padding: 20
            orientation: 'vertical'
            spacing: 15

            MDLabel:
                text: "📉 LIVE MULTI-VARIABLE OUTPUT"
                bold: True
                text_color: 0.9, 0.6, 0.1, 1
            
            MDBoxLayout:
                orientation: 'vertical'
                spacing: 8
                MDLabel:
                    text: "• Safety Car Probability: 64% (Sector 2 Dynamic Event)"
                    font_style: "Caption"
                MDLabel:
                    text: "• Fuel Optimization Target: Delta -0.04kg/Lap"
                    font_style: "Caption"
                MDLabel:
                    text: "• Estimated Target Output Ranking: P1 🔥"
                    font_style: "Body2"
                    bold: True
                    text_color: 0.2, 0.9, 0.2, 1

            MDRaisedButton:
                text: "🔄 RE-CALCULATE MATRIX"
                size_hint_x: 1
                md_bg_color: 0.2, 0.8, 0.2, 1
                on_release: root.manager.current = 'main_menu'
'''

class MainMenuScreen(Screen):
    pass

class RaceCenterScreen(Screen):
    pass

class SimulationScreen(Screen):
    pass

class AnalyticsScreen(Screen):
    pass

class F1NexusApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

if __name__ == '__main__':
    F1NexusApp().run()