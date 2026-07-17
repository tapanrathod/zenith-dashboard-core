# main.py
import sys
import time
from engine import MetricsEngine
from renderer import TerminalRenderer

def run_application():
    engine = MetricsEngine()
    engine.start()
    
    # Hide terminal cursor during execution for absolute layout smoothness
    sys.stdout.write(TerminalRenderer.HIDE)
    sys.stdout.flush()
    
    try:
        while True:
            # Capture snapshot from memory thread safely
            current_data = engine.get_latest_snapshots()
            
            # Form graphic matrix
            rendered_frame = TerminalRenderer.format_dashboard(current_data)
            
            # Draw frame block out to systemic standard stream
            sys.stdout.write(rendered_frame)
            sys.stdout.flush()
            
            # Lock loop standard cycle latency (60 updates per second potential)
            time.sleep(0.2)
            
    except KeyboardInterrupt:
        pass
    finally:
        engine.stop()
        # Restore user terminal defaults safely
        sys.stdout.write(TerminalRenderer.SHOW + TerminalRenderer.CLR)
        sys.stdout.flush()
        print(f"\n{TerminalRenderer.YELLOW}[INFO] Hardware tracking context closed down cleanly.{TerminalRenderer.RESET}\n")

if __name__ == "__main__":
    run_application()
