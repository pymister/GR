<template>
  <div class="home">
    <Header/>
    <Banner/>
    <Footer/>
  </div>
</template>

<script>
    import Header from './common/Header'
    import Banner from './common/Banner'
    import Footer from './common/Footer'
    export default {
        name: "Home",
        date(){
            return{

            };
        },
        components:{
            Header,
            Banner,
            Footer,
        }
    }
</script>

<style scoped>

</style>
