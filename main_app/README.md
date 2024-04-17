# 🌴 Wonderlust App 🌴

Wonderlust a travel-focused web application that allows users to create, manage, and share their travel experiences. Users can add postcards, upload photos, and mark locations on a map using markers. Helping users preserve their memories with a digital scrapbook.

- **Create Postcards**: Users can compose postcards by adding text, images, and location details.
- **Delete Postcards**: Postcards can be removed if no longer needed.
- **Upload Photos**: Users can attach photos to their postcards.
- **Map Integration**: The app displays a map with markers representing various travel locations.

## Technologies Used

- **Django**: A high-level Python web framework that simplifies building robust web applications.
- **JavaScript (Google Map API)**: Used for integrating maps and markers.
- **PostgreSQL (psql)**: The chosen database management system.
- **CSRF (Cross-Site Request Forgery) Protection**: Ensures secure communication between the client and server. CSRF tokens are used to authenticate and authorize users.
- **Materialize CSS**: A responsive front-end framework that provides beautiful styling and components for your app.

## ⚡ Installation ⚡

.env file in the root directory of the project and add the following variables:

- AWS_ACCESS_KEY_ID=yourkeygoeshere (If you like images or other media content)
- AWS_SECRET_ACCESS_KEY=yourkeygoeshere (If you like images or other media content)
- S3_BASE_URL=https://s3.(region).amazonaws.com/ (Location of S3 bucket)
- S3_BUCKET=yourbucknamegoeshere (If you like images or other media content)
- GOOGLE_MAPS_API_KEY=yourgooglemapaipkeygoeshere (If you want to use Google Maps and the markers)

<p>
  <img src="https://imgur.com/ZpjGyA9" width="350" title="SeiRocks!">
  <img src="https://imgur.com/a/mN1KZYX" width="350" title="SeiStillRocks!">
</p>

## Getting Started

#### 🌎✈️📸 [App Link ]<https://wonderlust-o8kk.onrender.com>

#### 📁 [Trello Link]<https://trello.com/b/JLxuOOJw/wonderlust>

#### 🔗 [Pitch Deck Link]<https://docs.google.com/presentation/d/1lvJuhyjvio_If_wsSDsVvugfufD61L5w/edit?usp=share_link&ouid=117169955102851300296&rtpof=true&sd=true>

## Next Steps: Planned Future Enhancements

- User to user engagement (likes, polling, etc.)
- Trip Planning
