echo '# Changelog' > CHANGELOG.md
echo '' >> CHANGELOG.md
echo '## v1.0 — Initial Release' >> CHANGELOG.md
echo '- Added main.py and README' >> CHANGELOG.md
git add CHANGELOG.md
git commit -m "docs: add changelog file"
git push
