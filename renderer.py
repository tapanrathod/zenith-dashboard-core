# renderer.py
import os

class TerminalRenderer:
    # Color Configuration Constants
    CLR = "\033[2J\033[H"
    HIDE = "\033[?25l"
    SHOW = "\033[?25h"
    RESET = "\033[0m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"

    @classmethod
    def make_progress_bar(cls, value, length=24):
        clamped = max(0.0, min(100.0, value))
        filled = int(length * clamped / 100)
        bar_string = "█" * filled + "░" * (length - filled)
        
        if clamped < 50:
            color = cls.GREEN
        elif clamped < 80:
            color = cls.YELLOW
        else:
            color = cls.RED
            
        return f"{color}[{bar_string}] {clamped:5.1f}%{cls.RESET}"

    @classmethod
    def format_dashboard(cls, data):
        frame = []
        frame.append(cls.CLR)
        frame.append(f"{cls.CYAN}┌────────────────────────────────────────────────────────────┐{cls.RESET}")
        frame.append(f"{cls.CYAN}│     ZENITH DISTRIBUTED MONITOR // MULTI-THREAD CORE        │{cls.RESET}")
        frame.append(f"{cls.CYAN}└────────────────────────────────────────────────────────────┘{cls.RESET}")
        
        frame.append(f" SYSTEM_UPTIME: {cls.MAGENTA}{data['uptime']}s{cls.RESET} | STATUS: {cls.GREEN}POLLING{cls.RESET} | PID: {os.getpid()}")
        frame.append(f"─" * 62)
        
        frame.append(f"\n{cls.CYAN}[PROCESSING UNITS]{cls.RESET}")
        for idx, core in enumerate(data["cores"]):
            frame.append(f"  ⚡ Core-0{idx} :: {cls.make_progress_bar(core)}")
            
        frame.append(f"\n{cls.CYAN}[MEMORY RESOURCE POOL]{cls.RESET}")
        frame.append(f"  💾 RAM Swap :: {cls.make_progress_bar(data['ram'], length=30)}")
        
        frame.append(f"\n{cls.CYAN}[NETWORK PIPELINE INTERFACES]{cls.RESET}")
        frame.append(f"  📥 RX Data Stream : {cls.GREEN}{data['network_in']:.2f} Mbps{cls.RESET}")
        frame.append(f"  📤 TX Data Stream : {cls.YELLOW}{data['network_out']:.2f} Mbps{cls.RESET}")
        
        frame.append(f"\n" + "─" * 62)
        frame.append(f"{cls.RED} » Signal execution kill sequence via Ctrl+C {cls.RESET}")
        
        return "\n".join(frame)
