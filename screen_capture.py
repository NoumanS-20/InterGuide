import mss
from PIL import Image

class ScreenCapture:
    """Captures screenshots for visual analysis"""
    
    def __init__(self):
        self.sct = mss.mss()
        
    def capture_screen(self, monitor_number=1):
        """
        Capture a screenshot of the specified monitor
        
        Args:
            monitor_number: Monitor to capture (1 = primary, 0 = all monitors)
            
        Returns:
            PIL.Image: Screenshot image
        """
        try:
            # Get the monitor
            monitor = self.sct.monitors[monitor_number]
            
            # Capture the screen
            sct_img = self.sct.grab(monitor)
            
            # Convert to PIL Image
            img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
            
            return img
            
        except Exception as e:
            print(f"Error capturing screen: {e}")
            return None
    
    def capture_region(self, left, top, width, height):
        """
        Capture a specific region of the screen
        
        Args:
            left, top, width, height: Region coordinates
            
        Returns:
            PIL.Image: Screenshot image
        """
        try:
            monitor = {
                "left": left,
                "top": top,
                "width": width,
                "height": height
            }
            
            sct_img = self.sct.grab(monitor)
            img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
            
            return img
            
        except Exception as e:
            print(f"Error capturing region: {e}")
            return None
    
    def list_monitors(self):
        """List all available monitors"""
        print("\nAvailable monitors:")
        for i, monitor in enumerate(self.sct.monitors):
            print(f"  Monitor {i}: {monitor}")
        return self.sct.monitors
