

// define html elements used
const cookieBanner = document.getElementById("cookie-banner");
const cookieBannerButton = document.getElementById("cookie-banner-button");

if (!Cookies.get("accepted-cookies-consent")) {
  // hide 'accept cookies' banner, if user gives consent to use cookies
  cookieBanner.classList.remove("cookie-banner--hide");
}

// onclick event will create 'enable cookies' cookie
cookieBannerButton.onclick = function() {
  Cookies.set("accepted-cookies-consent", true, { expires: 7 });
  cookieBanner.classList.add("cookie-banner--hide");
};

/**
 * optional
 * 
 */
