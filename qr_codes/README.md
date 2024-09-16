# Generate QR codes

> Generate a QR code as an PNG file

## Run in GitHub

1. Go to the `Actions` tab at the top of this repository
1. In the left bar, select the `Generate QR code` workflow
1. Click the gray `Run workflow` button on the right side, providing inputs as-needed:

   - `branch` should be left as `main`
   - `data` is required, this is the URL the QR code should point to
   - `color`, `background`, and `size` are optional

1. Click the green `Run workflow` button
1. Refresh the page to see the in-progress workflow run
1. When the workflow has completed (look for the green check mark), click the run
1. In the bottom pane under `Artifacts`, find a link to download the QR code image (downloads a ZIP file with the image inside)

## Run locally

1. Open this repository's devcontainer in VS Code
2. Change into the `qr_codes` directory
3. Run the helper script

```bash
$ python main.py -h
usage: main.py [-h] [--color COLOR] [--background BACKGROUND] [--size SIZE] data output

Generate a QR code as an PNG file

positional arguments:
  data                  The data to encode as a QR code
  output                Path to an PNG file where the QR code is written

options:
  -h, --help            show this help message and exit
  --color COLOR         The color of the QR code in hex format, by default black
  --background BACKGROUND
                        The background color of the QR code in hex format, by default transparent
  --size SIZE           The QR code size from 1-10, by default 4
```
