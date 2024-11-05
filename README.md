<!DOCTYPE html>
<html lang="en">
<body>
  <h1>People Detection at Entry Point Using YOLOv8</h1>
  <p>This project implements a people detection system at an entry point using the YOLOv8 model. The purpose is to identify and count people passing through a designated area, such as an entrance door, which can be useful for monitoring foot traffic, security, or crowd management.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>Real-Time Detection</strong>: Efficiently detects people in live video feeds using YOLOv8.</li>
    <li><strong>Count Monitoring</strong>: Tracks the count of people detected in the entry area.</li>
    <li><strong>Configurable</strong>: Easily adjust model parameters and settings to fit different environments.</li>
    <li><strong>Customizable Zones</strong>: Set detection areas and enhance model performance with custom data.</li>
  </ul>

  <h2>Getting Started</h2>
  <h3>Requirements</h3>
  <ul>
    <li>Python 3.8 or later</li>
    <li>Libraries: <code>ultralytics</code>, <code>opencv-python</code>, <code>torch</code></li>
    <li>Optional: GPU support for faster inference (requires CUDA-compatible device)</li>
  </ul>

  <h3>Installation</h3>
  <ol>
    <li><strong>Clone the Repository:</strong>
      <pre><code>git clone https://github.com/riskyasyam/people-detection-yolov8.git
cd people-detection-yolov8</code></pre>
    </li>
    <li><strong>Install Dependencies:</strong>
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
  </ol>

  <h2>Model Setup</h2>
  <p>Download YOLOv8 pre-trained weights from <a href="https://github.com/ultralytics/ultralytics">Ultralytics YOLOv8</a> or use your custom-trained model. Save the weights in the <code>models/</code> directory.</p>

  <h2>Usage</h2>
  <ol>
    <li><strong>Run Detection Script:</strong>
      <pre><code>python detect.py --source &lt;input_video&gt; --weights &lt;path_to_weights&gt; --conf 0.5</code></pre>
      <ul>
        <li><code>&lt;input_video&gt;</code>: Path to video file or camera feed URL.</li>
        <li><code>&lt;path_to_weights&gt;</code>: Path to YOLOv8 weights file.</li>
        <li><code>--conf</code>: Detection confidence threshold (e.g., 0.5).</li>
      </ul>
    </li>
    <li><strong>Parameter Adjustment:</strong> Update parameters in <code>detect.py</code> to optimize detection accuracy in different environments.</li>
  </ol>

  <h2>Configuration</h2>
  <ul>
    <li><strong>Detection Zone</strong>: Set a region of interest (ROI) to focus detection on specific areas.</li>
    <li><strong>Counting Logic</strong>: Customize the people-counting algorithm for entry and exit counting.</li>
  </ul>

  <h2>Project Structure</h2>
  <ul>
    <li><code>detect.py</code>: Main detection script.</li>
    <li><code>requirements.txt</code>: Python dependencies.</li>
    <li><code>README.md</code>: Project documentation.</li>
    <li><code>models/</code>: Directory for storing YOLOv8 weights.</li>
    <li><code>examples/</code>: Sample media files for testing.</li>
  </ul>

  <h2>Example Output</h2>
  <div class="image-container">
    <img src="examples/detection_screenshot.png" alt="Detection Example" width="600">
  </div>

  <h2>Future Enhancements</h2>
  <ul>
    <li><strong>Database Integration</strong>: Store detection logs for further analysis.</li>
    <li><strong>Alert System</strong>: Trigger alerts if a specified count is exceeded.</li>
    <li><strong>Dashboard</strong>: Develop a web interface to visualize and manage data.</li>
  </ul>

  <h2>Acknowledgements</h2>
  <p>Thanks to <a href="https://github.com/ultralytics/ultralytics">Ultralytics</a> for providing YOLOv8 and to OpenCV and PyTorch for video processing support.</p>

  <h2>License</h2>
  <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more information.</p>
</body>
</html>
