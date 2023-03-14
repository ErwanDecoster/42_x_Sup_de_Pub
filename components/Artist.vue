<!-- exemple d'utilisation :
<Artist 
  name="MICHEL POLNAREFF"
  description="Sa voix, intacte, et son sensationnel jeu de piano, font tout..."
  img="icone_twitter.svg"
  theme="MUSIQUE"
  days="16-17"
  month="06"
  fontSize="22"
/> -->

<template>
  <div class="flex flex-col gap-6 h-[530px] w-[350px] bg-">
    <div class="relative">
      <img 
        class="h-[350px] w-[350px]"
        :src="'/_nuxt/public/' + img"
        alt=""
      >
      <svg 
        class="absolute bottom-0 left-0 h-24 w-24" 
        viewBox="0 0 100 100"
      >
        <path 
          d="M 0,100 L 100,100 A 100,100 0 0 0 0,0 Z" 
          fill="#011627"
        />
      </svg>
      <p 
        class="absolute text-white text-4xl font-bold left-0 bottom-9"
        :style="{ 'font-size': fontSize + 'px' }"
      >
        {{ days }}
      </p>
      <p class="absolute text-white text-4xl font-bold left-7 bottom-0">
        {{ month }}
      </p>
    </div>
    <p class="bg-alizarin-crimson text-white text-base font-bold px-2 py-1 w-fit">
      {{ theme }}
    </p>
    <p class="text-white text-xl font-bold">
      {{ name }}
    </p>
    <p class="text-white text-base font-normal">
      {{ description }}
    </p>
  </div>
</template>

<script>
export default {
  props: { 
    name: {
      type: String,
      default: 'no name',
    },
    description: {
      type: String,
      default: 'no description',
    },
    img: {
      type: String,
      default: '',
    },
    theme: {
      type: String,
      default: '',
    },
    days: {
      type: String,
      default: '',
    },
    month: {
      type: String,
      default: '',
    },
    fontSize: {
      type: String,
      default: '35',
    },
  },
};
</script>