from getpdf import split_n, download_pdf
data=split_n()
for url in data[10:20]:
    download_pdf(url)

