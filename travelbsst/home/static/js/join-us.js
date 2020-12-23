class joinus extends HTMLElement {
    constructor(){
        super();
     
     
       this.innerHTML = localStorage.getItem("join-us-content");
       
    }
}
  
customElements.define("join-us", joinus);



