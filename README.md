# NCM Solutions (TM) - Full-Stack Python & Web Development

Modern static website for NCM Solutions showcasing Python and web development services. Features a responsive design with glass morphism effects, project showcase, and a working contact form with Netlify Forms integration.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Features

- Responsive single-page design.
- Projects/portfolio section.
- Contact form with Netlify Forms and mailto fallback.
- SVG logo and assets.
- SEO and Open Graph meta tags.
- Modern CSS with fluid typography and smooth interactions.

## Quick Launch

1. Double-click the "NCM Solutions Website" shortcut on your desktop to launch the local site (Windows).

   - The included shortcut starts a simple local server and opens the default browser.
   - Close the command window when you're done.

## Run Manually

1. Open `index.html` directly in your browser:

   - Windows: Right-click -> Open with -> your browser
   - Or use the included launcher script: `launch_website.bat`

For development (recommended):

```powershell
# Start a simple local static server from the project root
python -m http.server 8000
# Then open http://localhost:8000 in your browser
```

## Deploy to Netlify (Recommended)

1. Push this project to a GitHub repository (create a new repo and push the files in this folder).

2. Prepare domain (optional):

   - Buy a domain from any registrar (Namecheap, Google Domains, GoDaddy, Cloudflare, etc.).
   - Replace the `CNAME` file's placeholder with your purchased domain (one line) before deploying. This project uses `cm-logistics.net` as the example production domain.

3. Deploy on Netlify:

   - Sign in to Netlify and click "Add new site -> Import from Git".
   - Choose your Git provider and repository, set the branch to `main` (or whatever branch you use).
   - Netlify will deploy the static site from the repository root (no build command required).
   - After deploy, go to Site settings -> Domain management to add your custom domain or enable Netlify DNS.

4. Configure DNS at your registrar:

   - For Netlify-managed DNS: follow Netlify's prompts to transfer or set nameservers.
   - For external DNS: add a CNAME record for `www` pointing to your Netlify subdomain (example: `yoursite.netlify.app`) and an ALIAS/ANAME root record if supported, or set up Netlify recommended DNS records.

5. Netlify Forms:

   - The contact form is configured for Netlify Forms (`data-netlify="true"` and hidden `form-name` input).
   - After deployment, Netlify will auto-detect the form; you can inspect submissions in the Netlify dashboard.

6. Post-deploy checks:

   - Verify your site (example: `https://cm-logistics.net`) is serving the site and `sitemap.xml` and `robots.txt` are reachable.

Notes: Netlify handles SSL automatically. If you prefer GitHub Pages or another host, follow their DNS instructions. Netlify is recommended because it supports static hosting, automatic SSL, and Netlify Forms out of the box.

## Alternative Deployment

- GitHub Pages: Enable in repository settings (use `main` branch). Note: Contact form will use mailto fallback.

- Any static host: Upload files to your web server. Contact form uses mailto by default or update `script.js` to use Formspree/custom endpoint.

## Files

- `index.html` — Single-page site with all sections.
- `styles.css` — Modern, responsive styles.
- `script.js` — Form handling (Netlify + fallback).
- `assets/` — Logo, favicon, and OG image.

## Contact form

The contact form is pre-configured for Netlify Forms with a mailto fallback. Options:

1. Netlify deployment: Forms work automatically.
2. Formspree: Replace fetch call in `script.js` with your endpoint.
3. Custom API: Update fetch configuration in `script.js`.
4. Mailto fallback: Always works (current contact: `millerclay46@gmail.com`).

## Git workflow

### Local -> Remote Sync

To keep your local repository in sync with GitHub:

1. Before starting work:

```powershell
git pull origin main  # Get latest changes
```

2. Make your changes locally.

3. Stage and commit:

```powershell
git add .  # Stage all changes
# OR git add specific-file.txt for specific files
git commit -m "Describe your changes here"
```

4. Push to GitHub:

```powershell
git push origin main
```

### Branch & PR Workflow

For safer changes and code review:

1. Create a new feature branch:

```powershell
git checkout -b feature-name
```

2. Make your changes in this branch.

3. Push branch to GitHub:

```powershell
git push origin feature-name
```

4. Create PR on GitHub: Use the GitHub UI (Compare & pull request) to open a PR, review, and merge.

## OneDrive sync tips

For avoiding sync conflicts:

- Add `.gitignore` for OneDrive temp files (example included in this repo).
- Avoid editing while syncing: wait for OneDrive to finish before making edits.
- Best practice: keep the Git repo outside OneDrive if possible.

## Next steps

1. Add your actual project screenshots/links.
2. Add company description and team section.
3. Add blog/articles section.
4. Add analytics.
5. Add more interactive features.
