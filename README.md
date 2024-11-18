<h1>CR2 to JPEG Converter</h1>

<p>This Python script converts <code>.cr2</code> (Canon Raw Image) files to <code>.jpeg</code> format. It uses the <code>rawpy</code> library for raw image processing and the <code>PIL</code> library (Pillow) for saving the images in JPEG format.</p>

<h2>Requirements</h2>

<p>Before running the script, make sure to install the necessary dependencies:</p>
<ul>
  <li><code>rawpy</code>: A Python wrapper for reading RAW files.</li>
  <li><code>Pillow</code>: A popular Python Imaging Library (PIL Fork).</li>
</ul>

<p>You can install them using <code>pip</code>:</p>
<pre><code>pip install rawpy Pillow</code></pre>

<h2>Usage</h2>

<h3>Command-line Usage</h3>

<ol>
  <li>Clone or download the repository.</li>
  <li>Open a terminal (or Command Prompt on Windows).</li>
  <li>Navigate to the directory where the script is located.</li>
  <li>Run the script using the following command:</li>
</ol>

<pre><code>python transform.py [input_directory]</code></pre>

<ul>
  <li><code>input_directory</code>: (Optional) The directory containing <code>.cr2</code> files. If not provided, the script will use the current working directory.</li>
</ul>

<p>For example:</p>

<pre><code>python transform.py /path/to/cr2/files</code></pre>

<p>If the directory is not provided, it defaults to the current working directory:</p>

<pre><code>python transform.py</code></pre>

<h3>Output</h3>

<ul>
  <li>The script will create a new directory called <code>images</code> in the provided directory (or the current working directory if no input directory is specified).</li>
  <li>Each <code>.cr2</code> file will be converted into a <code>.jpeg</code> file with the same name (except the extension) inside the <code>images</code> folder.</li>
</ul>

<p>For example, if you have a file named <code>photo.cr2</code>, it will be converted to <code>photo.jpeg</code> and placed in the <code>images</code> folder.</p>

<h3>Error Handling</h3>

<p>If an error occurs while converting any <code>.cr2</code> file, the script will print an error message to the terminal and continue with the next file.</p>


