<template>
  <div
    id="navbar"
    data-scroll="0"
    class="duration-200 fixed z-20 h-32 w-full hidden lg:flex py-3"
  >
    <div class="justify-between max-w-screen-xl m-auto w-full flex px-6">
      <NuxtLink to="/">
        <img
          class="h-full"
          src="@/src/logo.svg"
          alt=""
        >
      </NuxtLink>
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
          to="/programming_and_ticketing"
          class="button-primary"
        >
          PROGRAMMATION & BILLETTERIE
        </NuxtLink>
        <NuxtLink
          to="/basket"
          class="h-11 w-11 bg-maximum-blue-green rounded-full text-sm px-5 py-2 border-2 border-maximum-blue-green font-medium uppercase cursor-pointer duration-150 group hover:bg-transparent flex justify-center flex-col items-center"
        >
          <svg
            viewBox="0 0 17 16" 
            fill="none" 
            xmlns="http://www.w3.org/2000/svg"
            class=" h-6 w-6"
          >
            <path 
              class="group-hover:fill-maximum-blue-green duration-150" 
              d="M0.599609 1.25293C0.636117 1.18874 0.665805 1.12014 0.709936 1.06157C0.834304 0.894673 0.997186 0.79919 1.21262 0.799993C1.88501 0.801999 2.55781 0.797987 3.2302 0.801999C3.53871 0.803603 3.75856 0.972905 3.83318 1.27259C4.0073 1.97106 4.18141 2.66953 4.33707 3.37241C4.37559 3.54652 4.45061 3.58102 4.61028 3.58102C7.50846 3.57822 10.4066 3.58062 13.3048 3.58102C14.303 3.58102 15.3011 3.57822 16.2993 3.57942C16.8168 3.58022 17.0836 3.91802 16.9648 4.4179C16.889 4.73644 16.8084 5.05378 16.7298 5.37152C16.3286 6.98951 15.923 8.6067 15.5298 10.2267C15.4423 10.5866 15.2478 10.8385 14.7683 10.8373C11.6567 10.8281 8.54473 10.8325 5.43312 10.8321C5.02551 10.8321 4.82371 10.6748 4.72983 10.2829C4.27168 8.3708 3.81392 6.45874 3.35657 4.54668C3.17042 3.76838 2.98387 2.99008 2.80454 2.20977C2.77164 2.06654 2.71467 2.01278 2.55941 2.0176C2.13295 2.03043 1.70568 2.0192 1.27842 2.02321C0.974318 2.02602 0.756474 1.90326 0.640932 1.6148C0.634513 1.59755 0.613651 1.58672 0.599609 1.57308C0.599609 1.46637 0.599609 1.35965 0.599609 1.25293ZM10.1467 4.80745C8.4332 4.80745 6.71972 4.80745 5.00625 4.80745C4.94206 4.80745 4.87787 4.81026 4.81408 4.80625C4.71258 4.79943 4.68129 4.83594 4.70977 4.93784C4.75511 5.10112 4.78921 5.26722 4.82853 5.4321C5.15028 6.77849 5.47283 8.12487 5.79258 9.47166C5.81625 9.57075 5.84875 9.61569 5.9683 9.61569C8.7385 9.61087 11.5087 9.61127 14.2793 9.61408C14.386 9.61408 14.4229 9.58078 14.4454 9.47607C14.5128 9.16034 14.595 8.84741 14.6729 8.53408C14.9681 7.34496 15.2614 6.15544 15.5639 4.96833C15.6016 4.82029 15.5651 4.80465 15.4307 4.80505C13.6691 4.80906 11.9079 4.80786 10.1463 4.80786L10.1467 4.80745Z" 
              fill="#011627"
            />
            <path 
              class="group-hover:fill-maximum-blue-green duration-150" 
              d="M11.542 13.758C11.5448 12.6274 12.4615 11.7163 13.5868 11.7175C14.7691 11.7187 15.6453 12.7125 15.6277 13.7768C15.6088 14.9066 14.7042 15.8072 13.5684 15.8C12.4479 15.7932 11.5396 14.8773 11.5424 13.758H11.542ZM12.772 13.756C12.7696 14.2025 13.1343 14.5752 13.5764 14.5784C14.0229 14.5816 14.4057 14.2029 14.4053 13.7576C14.4053 13.3207 14.0269 12.9452 13.5864 12.9448C13.1395 12.9448 12.7744 13.3082 12.7716 13.756H12.772Z" 
              fill="#011627"
            />
            <path 
              class="group-hover:fill-maximum-blue-green duration-150" 
              d="M6.16061 11.7187C7.24101 11.7139 8.21028 12.574 8.20707 13.7732C8.20426 14.9085 7.27872 15.8056 6.14777 15.7996C5.02525 15.7936 4.1286 14.8813 4.12017 13.7619C4.11215 12.6751 5.01723 11.7095 6.16021 11.7187H6.16061ZM6.97462 13.7587C6.97462 13.3082 6.61275 12.9451 6.16382 12.9443C5.71288 12.9435 5.33296 13.325 5.34138 13.77C5.34981 14.2117 5.72813 14.582 6.16703 14.578C6.61475 14.5735 6.97542 14.2081 6.97502 13.7587H6.97462Z" 
              fill="#011627"
            />
          </svg>
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