 
 


 var link_ge = localStorage.getItem("link_ge");
 var link_ukr = localStorage.getItem("link_ukr");
 var link_tur = localStorage.getItem("link_tur");



 $(".country_link_ge").prop("href",link_ge);
 $(".country_link_ukr").prop("href", link_ukr);
 $(".country_link_tur").prop("href", link_tur);

 $(".country_link_ge_footer").prop("href",link_ge+"#countrycommunities");
 $(".country_link_ukr_footer").prop("href", link_ukr+"#countrycommunities");
 $(".country_link_tur_footer").prop("href", link_tur+"#countrycommunities");
 

 