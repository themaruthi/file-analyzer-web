import os
import shutil
from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def run_analysis(upload_dir, output_dir):
    summary_path = os.path.join(output_dir, 'summary.txt')
    archive_path = os.path.join(output_dir, 'text_files_archive.tar.gz')

    files = [os.path.join(upload_dir, f) for f in os.listdir(upload_dir) if f.endswith('.txt')]
    file_stats = []

    for file in files:
        error_count = 0
        total_lines = 0
        try:
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    total_lines += 1
                    if 'error' in line.lower():
                        error_count += 1
        except:
            continue

        wc_result = subprocess.run(['wc', '-l', file], stdout=subprocess.PIPE, text=True)
        wc_lines = int(wc_result.stdout.strip().split()[0])
        file_stats.append((file, error_count, total_lines, wc_lines))

    # Write summary
    with open(summary_path, 'w') as out:
        for fname, errors, py_lines, wc_lines in file_stats:
            out.write(f"File: {os.path.basename(fname)}\n")
            out.write(f"Error Count (Python): {errors}\n")
            out.write(f"Total Lines (Python): {py_lines}\n")
            out.write(f"Total Lines (wc -l): {wc_lines}\n")
            out.write(f"Discrepancy: {'Yes' if py_lines != wc_lines else 'No'}\n")
            out.write("=" * 40 + "\n")

    # Create archive
    subprocess.run(['tar', '-czf', archive_path, '-C', upload_dir, '.'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Clear old uploads/output
        shutil.rmtree(UPLOAD_FOLDER)
        shutil.rmtree(OUTPUT_FOLDER)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        # Save files
        for file in request.files.getlist('files'):
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        # Run analysis
        run_analysis(UPLOAD_FOLDER, OUTPUT_FOLDER)
        return redirect(url_for('results'))

    return render_template('index.html')

@app.route('/results')
def results():
    with open(os.path.join(OUTPUT_FOLDER, 'summary.txt')) as f:
        summary = f.read()
    return render_template('index.html', summary=summary)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
