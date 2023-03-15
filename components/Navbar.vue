<template>
  <div
    id="navbar"
    data-scroll="0"
    class="duration-200 fixed z-20 h-32 w-full hidden lg:flex py-3"
  >
    <div class="justify-between max-w-screen-xl m-auto w-full flex px-6">
      <img
        class="h-full"
        src="@/src/logo.svg"
        alt=""
      >
      <div class="flex gap-4 xl:gap-12 items-center ">
        <NuxtLink
          to="/about_us"
          class="button-simple "
        >
          QUI SOMMES-NOUS ?
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-simple "
        >
          INFOS PRATIQUES
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-primary"
        >
          PROGRAMMATION & BILLETTERIE
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-primary-two px-2 hover:bg-maximum-blue-green"
        >
          <img
            class="h-5 w-6"
            src="@/src/icone_panier_noir.svg"
            alt=""
          >
        </NuxtLink>
      </div>
    </div>
  </div>
</template>



<script>
export default {
  data() {
    return {
      fullNavOpen: false,
    };
  },
  mounted() {
    document.documentElement.dataset.scroll = window.scrollY;
    window.addEventListener('scroll', () => {
      document.documentElement.dataset.scroll = window.scrollY;
    });
  }
};
</script>

<style>
html:not([data-scroll='0']) #navbar {
  background: #011627;
  padding-top: 8px;
  padding-bottom: 8spx;
  height: 96px;
}
</style>