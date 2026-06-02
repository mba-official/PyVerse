import os
import io

import fitz  # PyMuPDF
from PIL import Image

INPUT_FOLDER = "pdfs"
OUTPUT_FOLDER = "compressed"

TARGET_SIZE_MB = 1.8

# Compression quality attempts
QUALITIES = [45, 35, 25]
DPIS = [80, 60]

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def get_size_mb(path):
    return os.path.getsize(path) / (1024 * 1024)


def compress_pdf(input_path, output_path):

    original_size = get_size_mb(input_path)

    print("\n" + "=" * 60)
    print(f"📄 Processing: {os.path.basename(input_path)}")
    print(f"📦 Original size: {original_size:.2f} MB")
    print("=" * 60)

    # More aggressive settings
    DPIS = [50, 40, 30]
    QUALITIES = [20, 15, 10]

    success = False
    best_size = 999

    for dpi in DPIS:

        for quality in QUALITIES:

            try:

                doc = fitz.open(input_path)

                images = []

                zoom = dpi / 72
                matrix = fitz.Matrix(zoom, zoom)

                for page in doc:

                    pix = page.get_pixmap(
                        matrix=matrix,
                        colorspace=fitz.csGRAY  # grayscale
                    )

                    img = Image.frombytes(
                        "L",  # grayscale
                        [pix.width, pix.height],
                        pix.samples
                    )

                    # Additional resize reduction
                    width, height = img.size

                    img = img.resize(
                        (
                            int(width * 0.7),
                            int(height * 0.7)
                        ),
                        Image.LANCZOS
                    )

                    img_bytes = io.BytesIO()

                    img.save(
                        img_bytes,
                        format="JPEG",
                        quality=quality,
                        optimize=True
                    )

                    compressed_img = Image.open(
                        io.BytesIO(img_bytes.getvalue())
                    )

                    images.append(compressed_img)

                images[0].save(
                    output_path,
                    save_all=True,
                    append_images=images[1:],
                    resolution=dpi
                )

                new_size = get_size_mb(output_path)

                print(
                    f"Trying DPI={dpi}, "
                    f"Quality={quality} "
                    f"-> {new_size:.2f} MB"
                )

                if new_size < best_size:
                    best_size = new_size

                if new_size <= TARGET_SIZE_MB:

                    print("\n✅ SUCCESS")
                    print(f"Final size: {new_size:.2f} MB")

                    success = True
                    return

            except Exception as e:

                print(f"\n❌ Failed: {e}")

    print("\n⚠️ Could not reach target size.")
    print(f"Best achieved size: {best_size:.2f} MB")


def main():

    pdf_files = [
        os.path.join(INPUT_FOLDER, f)
        for f in os.listdir(INPUT_FOLDER)
        if f.lower().endswith(".pdf")
    ]

    if not pdf_files:

        print(f"No PDFs found in '{INPUT_FOLDER}'")
        return

    for pdf in pdf_files:

        output_path = os.path.join(
            OUTPUT_FOLDER,
            os.path.basename(pdf)
        )

        compress_pdf(pdf, output_path)

    print("\n🎉 Done!")
    print(f"Compressed PDFs saved in '{OUTPUT_FOLDER}'")


if __name__ == "__main__":
    main()