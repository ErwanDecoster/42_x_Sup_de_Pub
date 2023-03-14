<template>
  <div 
    id="navbar"
    data-scroll="0"
    class="duration-200 fixed z-20 h-32 w-full flex py-6"
  >
    <div class="justify-between max-w-screen-xl m-auto w-full hidden lg:flex px-6">
      <img
        class="h-full"
        src="@/src/logo.svg"
        alt=""
      >
      <div class="flex gap-4 xl:gap-12 items-center ">
        <NuxtLink
          to=""
          class="button-simple "
        >
          QUI SOMMES NOUS?
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-simple "
        >
          INFOS PRATIQUES
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-simple "
        >
          PROGRAMMATION
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-primary"
        >
          BILLETERIE
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-primary-two "
        >
          pannier
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
