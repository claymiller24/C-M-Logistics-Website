
# C&M Logistics™ — Full-Stack Python & Web Development

Modern static website for C&M Logistics showcasing Python and web development services. Features a responsive design with glass morphism effects, project showcase, and a working contact form with Netlify Forms integration.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Features

- Responsive single-page design
- Projects/portfolio section
- Contact form with Netlify Forms and mailto fallback
- SVG logo and assets
- SEO and Open Graph meta tags
- Modern CSS with fluid typography and smooth interactions

## Quick Launch

1. Double-click the "C&M Logistics Website" shortcut on your desktop
   - This will start the server and open the website automatically
   - Close the command window when you're done

## Run Manually

1. Open `index.html` directly in your browser:
   - Windows: Right-click → Open with → your browser
   - Or use the included launcher script: `launch_website.bat`

2. For development, you can also run the Python server manually:

```powershell
python -m http.server 8000
# Then open http://localhost:8000
```

## Deploy to Netlify (Recommended)

1. Push this project to a GitHub repository (create a new repo and push the files in this folder).

2. Prepare domain (optional):
   - Buy a domain from any registrar (Namecheap, Google Domains, GoDaddy, Cloudflare, etc.).
      - Replace the `CNAME` file's placeholder with your purchased domain (one line) before deploying. This project now uses `cm-logistics.net` as the example production domain.

3. Deploy on Netlify:
   - Sign in to Netlify and click "Add new site → Import from Git".
   - Choose your Git provider and repository, set branch to `main` (or whatever branch you use).
   - Netlify will deploy the static site from the repository root (no build command required).
   - After deploy, go to Site settings → Domain management to add your custom domain or enable Netlify DNS.

4. Configure DNS at your registrar:
   - For Netlify-managed DNS: follow Netlify's prompts to transfer or set nameservers.
      - For external DNS: add a CNAME record for `www` pointing to your Netlify subdomain (example: `yoursite.netlify.app`) and an ALIAS/ANAME root record if supported, or set up Netlify recommended DNS records. Example records for `cm-logistics.net` will be provided by Netlify during setup.

5. Netlify Forms:
   - The contact form is configured for Netlify Forms (`data-netlify="true"` and hidden `form-name` input).
   - After deployment, Netlify will auto-detect the form; you can inspect submissions in the Netlify dashboard.

6. Post-deploy checks:
      - Verify `https://cm-logistics.net` is serving the site and `sitemap.xml` and `robots.txt` are reachable.
      - `sitemap.xml` and `robots.txt` here already reference `cm-logistics.net`.

Notes: Netlify handles SSL automatically. If you prefer GitHub Pages or another host, follow their DNS instructions. Netlify is recommended because it supports static hosting, automatic SSL, and Netlify Forms out-of-the-box.

## Alternative Deployment

- GitHub Pages: Enable in repository settings (use `main` branch)
  - Note: Contact form will use mailto fallback
- Any static host: Upload files to your web server
  - Contact form uses mailto by default
  - Or update `script.js` to use Formspree/custom endpoint

## Files

- `index.html` — Single-page site with all sections
- `styles.css` — Modern, responsive styles
- `script.js` — Form handling (Netlify + fallback)
- `assets/` — Logo, favicon, and OG image

## Contact Form

The contact form is pre-configured for Netlify Forms with a mailto fallback. Options:

1. Netlify deployment: Forms work automatically
2. Formspree: Replace fetch call in `script.js` with your endpoint
3. Custom API: Update fetch configuration in `script.js`
4. Mailto fallback: Always works (current contact: `millerclay46@gmail.com`)

## Next Steps

1. Add your actual project screenshots/links
2. Add company description and team section
3. Add blog/articles section
4. Integrate analytics
5. Add more interactive features
