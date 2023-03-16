<template>
  <div>
    <section class="background w-full h-[100vh]">
      <!-- <img
        class="h-2/5 absolute -right-20 -top-2 -rotate-90"
        src="@/src/halfcircle.svg"
        alt=""
      > -->
      <div class="z-10 pt-[60vh] px-8 grid gap-6">
        <p class="text-white">
          <NuxtLink
            to="/"
            class="font-bold"
          >
            Acceuil
          </Nuxtlink> > Info pratique
        </p>
        <h1 class="uppercase text-8xl text-khaki font-bold w-3/4">
          INFOS<br>PRATIQUES
        </h1>
      </div>
    </section>
    <section class="flex mx-auto">
      <div class="flex flex-col max-w-screen-2xl mx-auto xl:gap-24 gap-8 xl:py-24 py-12">
        <div class="grid xl:grid-cols-5 w-full xl:gap-36 gap-6 p-6">
          <div class="flex flex-col gap-6 xl:order-1 xl:col-span-2">
            <img 
              class="w-auto sm:max-w-xl "
              src="@/src/image_4.png"
              alt=""
            >
            <p class="text-white text-base font-normal italic">
              Théâtre antique
            </p>
          </div>
          <div class="flex flex-col gap-12 xl:col-span-3">
            <div>
              <p class="text-white font-normal text-1xl lg:text-4xl md:text-3xl">
                VENIR AUX NUITS
              </p>
              <p class="whitespace-nowrap text-khaki font-bold text-2xl -mt-5 lg:text-5xl md:text-4xl">
                LUGDUNUM - THÉÂTRES ROMAINS
              </p>
            </div>
            <div class="flex flex-col gap-6">
              <p class="text-white text-base font-normal max-w-lg">
                6 rue de l'Antiquaille - Lyon 5e <br> <br> Depuis plusieurs années, les Nuits de Fourvière travaillent 
                avec leurs partenaires sur la thématique de la mobilité afin de préserver la qualité de vie du quartier 
                et de réduire les impacts environnementaux du festival.
              </p>
            </div>
            <div class="flex gap-6">
              <div class="flex flex-col items-center gap-2 md:gap-5">
                <div 
                  class="flex group hover:bg-maximum-blue-green duration-150 w-20 h-20 md:w-24 md:h-24 rounded-full border-4 border-maximum-blue-green justify-center items-center p-6 hover:cursor-pointer"
                  :class="`${ deplacement=='pied' ? 'bg-maximum-blue-green' : 'bg-maastricht-blue'}`"  
                  @click="deplacement = 'pied'"
                >
                  <svg width="32" height="60" viewBox="0 0 32 60" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                      :class="`${ deplacement=='pied' ? 'stroke-white' : 'stroke-maximum-blue-green'}`"
                      class="group-hover:stroke-white duration-150"
                      d="M14.8083 20.9736L10.4615 38.3703L25.6816 57.9405M8.28803 49.2437L1.76465 57.9374" 
                      stroke="#2EC4B6" 
                      stroke-width="3" 
                      stroke-linecap="round" 
                      stroke-linejoin="round"
                    />
                    <path 
                      :class="`${ deplacement=='pied' ? 'stroke-white' : 'stroke-maximum-blue-green'}`" 
                      class="group-hover:stroke-white duration-150"
                      d="M1.76465 34.0215C1.76465 21.8453 10.4615 20.9747 14.8114 20.9747H19.1583C19.8838 24.5992 23.0729 32.2834 30.0316 34.0215M16.5372 14.4081C18.1748 14.4081 19.7453 13.7576 20.9032 12.5996C22.0612 11.4417 22.7117 9.87119 22.7117 8.2336C22.7117 6.59602 22.0612 5.0255 20.9032 3.86756C19.7453 2.70961 18.1748 2.05908 16.5372 2.05908C14.8996 2.05908 13.3291 2.70961 12.1711 3.86756C11.0132 5.0255 10.3627 6.59602 10.3627 8.2336C10.3627 9.87119 11.0132 11.4417 12.1711 12.5996C13.3291 13.7576 14.8996 14.4081 16.5372 14.4081Z" 
                      stroke="#2EC4B6" 
                      stroke-width="3" 
                      stroke-linecap="round" 
                      stroke-linejoin="round"
                    />
                  </svg>
                </div>
                <p class="text-khaki text-base font-medium">
                  À pied
                </p>
              </div>
              <div class="flex flex-col items-center gap-2 md:gap-5">
                <div 
                  class="flex group hover:bg-maximum-blue-green duration-150 w-20 h-20 md:w-24 md:h-24 rounded-full border-4 border-maximum-blue-green justify-center items-center p-4 hover:cursor-pointer"
                  :class="`${ deplacement=='velo' ? 'bg-maximum-blue-green' : 'bg-maastricht-blue'}`"  
                  @click="deplacement = 'velo'"
                >
                  <svg width="58" height="50" viewBox="0 0 58 50" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path 
                      :class="`${ deplacement=='velo' ? 'fill-white' : 'fill-maximum-blue-green'}`"  
                      class="group-hover:fill-white duration-150" 
                      d="M37.9525 14.5833C39.3704 14.5833 40.7565 14.1557 41.9355 13.3545C43.1144 12.5532 44.0333 11.4144 44.5759 10.0821C45.1185 8.74969 45.2605 7.28358 44.9839 5.86914C44.7072 4.45469 44.0245 3.15544 43.0218 2.13568C42.0192 1.11593 40.7418 0.421461 39.3511 0.140111C37.9605 -0.14124 36.519 0.00315935 35.209 0.555048C33.899 1.10694 32.7794 2.04153 31.9916 3.24064C31.2038 4.43974 30.7834 5.84951 30.7834 7.29167C30.7834 9.22554 31.5387 11.0802 32.8832 12.4477C34.2276 13.8151 36.0511 14.5833 37.9525 14.5833ZM37.9525 4.16667C38.5602 4.16667 39.1542 4.34995 39.6595 4.69333C40.1647 5.03671 40.5586 5.52476 40.7911 6.09578C41.0236 6.6668 41.0845 7.29514 40.9659 7.90133C40.8474 8.50752 40.5548 9.06434 40.1251 9.50138C39.6954 9.93842 39.1479 10.236 38.5519 10.3566C37.9559 10.4772 37.3381 10.4153 36.7767 10.1788C36.2153 9.94227 35.7354 9.54173 35.3978 9.02782C35.0602 8.51392 34.88 7.90974 34.88 7.29167C34.88 6.46287 35.2037 5.66801 35.7799 5.08196C36.3561 4.49591 37.1376 4.16667 37.9525 4.16667ZM47.1699 29.1667C45.1443 29.1667 43.1642 29.7776 41.48 30.9222C39.7958 32.0668 38.4831 33.6936 37.7079 35.597C36.9328 37.5004 36.73 39.5949 37.1251 41.6155C37.5203 43.6362 38.4957 45.4922 39.928 46.949C41.3603 48.4058 43.1852 49.3979 45.1719 49.7998C47.1586 50.2018 49.2178 49.9955 51.0892 49.2071C52.9606 48.4187 54.5602 47.0835 55.6855 45.3705C56.8109 43.6575 57.4115 41.6436 57.4115 39.5833C57.4115 36.8207 56.3325 34.1711 54.4118 32.2176C52.4912 30.2641 49.8862 29.1667 47.1699 29.1667ZM47.1699 45.8333C45.9546 45.8333 44.7665 45.4668 43.756 44.78C42.7454 44.0933 41.9578 43.1171 41.4927 41.9751C41.0276 40.8331 40.9059 39.5764 41.1431 38.364C41.3802 37.1516 41.9654 36.038 42.8248 35.1639C43.6842 34.2898 44.7791 33.6946 45.9711 33.4534C47.1631 33.2123 48.3987 33.336 49.5215 33.8091C50.6444 34.2821 51.6041 35.0832 52.2793 36.111C52.9545 37.1388 53.3149 38.3472 53.3149 39.5833C53.3149 41.2409 52.6675 42.8306 51.5151 44.0027C50.3627 45.1748 48.7997 45.8333 47.1699 45.8333ZM10.3002 29.1667C8.2746 29.1667 6.29449 29.7776 4.61027 30.9222C2.92605 32.0668 1.61336 33.6936 0.838193 35.597C0.0630313 37.5004 -0.139786 39.5949 0.255388 41.6155C0.650562 43.6362 1.62598 45.4922 3.05829 46.949C4.49061 48.4058 6.31548 49.3979 8.30216 49.7998C10.2888 50.2018 12.3481 49.9955 14.2195 49.2071C16.0909 48.4187 17.6904 47.0835 18.8158 45.3705C19.9411 43.6575 20.5418 41.6436 20.5418 39.5833C20.5418 38.2154 20.2769 36.8609 19.7622 35.597C19.2475 34.3332 18.4931 33.1849 17.5421 32.2176C16.5911 31.2504 15.4621 30.4831 14.2195 29.9596C12.9769 29.4361 11.6451 29.1667 10.3002 29.1667ZM10.3002 45.8333C9.08484 45.8333 7.89677 45.4668 6.88624 44.78C5.87571 44.0933 5.08809 43.1171 4.62299 41.9751C4.1579 40.8331 4.03621 39.5764 4.27331 38.364C4.51042 37.1516 5.09567 36.038 5.95505 35.1639C6.81444 34.2898 7.90937 33.6946 9.10137 33.4534C10.2934 33.2123 11.5289 33.336 12.6518 33.8091C13.7746 34.2821 14.7343 35.0832 15.4095 36.111C16.0848 37.1388 16.4452 38.3472 16.4452 39.5833C16.4452 41.2409 15.7977 42.8306 14.6453 44.0027C13.4929 45.1748 11.9299 45.8333 10.3002 45.8333ZM45.1216 25H34.88C34.611 25.0002 34.3445 24.9465 34.0958 24.8419C33.8472 24.7374 33.6212 24.584 33.4308 24.3906L26.6867 17.5286L21.3893 22.9167L30.1843 31.8594C30.3744 32.053 30.5252 32.2828 30.628 32.5357C30.7308 32.7886 30.7836 33.0597 30.7834 33.3333V45.8333C30.7834 46.3859 30.5676 46.9158 30.1834 47.3065C29.7993 47.6972 29.2783 47.9167 28.7351 47.9167C28.1918 47.9167 27.6708 47.6972 27.2867 47.3065C26.9025 46.9158 26.6867 46.3859 26.6867 45.8333V34.1953L17.0443 24.3906C16.8538 24.1971 16.7028 23.9674 16.5997 23.7145C16.4966 23.4615 16.4435 23.1904 16.4435 22.9167C16.4435 22.6429 16.4966 22.3718 16.5997 22.1189C16.7028 21.866 16.8538 21.6362 17.0443 21.4427L25.2376 13.1094C25.4278 12.9157 25.6537 12.762 25.9024 12.6572C26.151 12.5523 26.4176 12.4984 26.6867 12.4984C26.9559 12.4984 27.2225 12.5523 27.4711 12.6572C27.7198 12.762 27.9457 12.9157 28.1359 13.1094L35.7275 20.8333H45.1216C45.6649 20.8333 46.1859 21.0528 46.57 21.4435C46.9541 21.8342 47.1699 22.3641 47.1699 22.9167C47.1699 23.4692 46.9541 23.9991 46.57 24.3898C46.1859 24.7805 45.6649 25 45.1216 25Z" 
                      fill="#2EC4B6"
                    />
                  </svg>
                </div>
                <p class="text-khaki text-base font-medium">
                  À vélo
                </p>
              </div>
              <div class="flex flex-col items-center gap-2 md:gap-5">
                <div 
                  class="flex group hover:bg-maximum-blue-green duration-150 w-20 h-20 md:w-24 md:h-24 rounded-full border-4 border-maximum-blue-green justify-center items-center p-4 hover:cursor-pointer"
                  :class="`${ deplacement=='bus' ? 'bg-maximum-blue-green' : 'bg-maastricht-blue'}`"
                  @click="deplacement = 'bus'"
                >
                  <svg width="49" height="49" viewBox="0 0 49 49" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                      :class="`${ deplacement=='bus' ? 'fill-white' : 'fill-maximum-blue-green'}`"  
                      class="group-hover:fill-white duration-150" 
                      d="M23.0022 6.93277C22.5425 6.93277 22.1017 7.11538 21.7767 7.44041C21.4516 7.76545 21.269 8.2063 21.269 8.66597C21.269 9.12564 21.4516 9.56648 21.7767 9.89152C22.1017 10.2166 22.5425 10.3992 23.0022 10.3992H26.4686C26.9283 10.3992 27.3691 10.2166 27.6942 9.89152C28.0192 9.56648 28.2018 9.12564 28.2018 8.66597C28.2018 8.2063 28.0192 7.76545 27.6942 7.44041C27.3691 7.11538 26.9283 6.93277 26.4686 6.93277H23.0022ZM19.5358 32.0641C19.5358 32.7536 19.2619 33.4149 18.7744 33.9024C18.2868 34.39 17.6255 34.6639 16.936 34.6639C16.2465 34.6639 15.5853 34.39 15.0977 33.9024C14.6102 33.4149 14.3363 32.7536 14.3363 32.0641C14.3363 31.3746 14.6102 30.7133 15.0977 30.2257C15.5853 29.7382 16.2465 29.4643 16.936 29.4643C17.6255 29.4643 18.2868 29.7382 18.7744 30.2257C19.2619 30.7133 19.5358 31.3746 19.5358 32.0641ZM32.5348 34.6639C33.2243 34.6639 33.8856 34.39 34.3731 33.9024C34.8607 33.4149 35.1346 32.7536 35.1346 32.0641C35.1346 31.3746 34.8607 30.7133 34.3731 30.2257C33.8856 29.7382 33.2243 29.4643 32.5348 29.4643C31.8453 29.4643 31.184 29.7382 30.6965 30.2257C30.2089 30.7133 29.935 31.3746 29.935 32.0641C29.935 32.7536 30.2089 33.4149 30.6965 33.9024C31.184 34.39 31.8453 34.6639 32.5348 34.6639ZM3.93709 10.0525C3.93709 7.38643 4.99619 4.82953 6.88141 2.94432C8.76662 1.0591 11.3235 0 13.9896 0H35.4812C38.1473 0 40.7042 1.0591 42.5894 2.94432C44.4746 4.82953 45.5337 7.38643 45.5337 10.0525V17.3319H47.2669C47.7266 17.3319 48.1674 17.5145 48.4925 17.8396C48.8175 18.1646 49.0001 18.6055 49.0001 19.0651C49.0001 19.5248 48.8175 19.9656 48.4925 20.2907C48.1674 20.6157 47.7266 20.7983 47.2669 20.7983H45.5337V44.0231C45.5337 45.2183 45.059 46.3645 44.2139 47.2095C43.3688 48.0546 42.2226 48.5294 41.0274 48.5294H36.1745C34.9793 48.5294 33.8331 48.0546 32.988 47.2095C32.143 46.3645 31.6682 45.2183 31.6682 44.0231V41.5966H17.8026V44.0231C17.8026 45.2183 17.3279 46.3645 16.4828 47.2095C15.6377 48.0546 14.4915 48.5294 13.2963 48.5294H8.44339C7.24825 48.5294 6.10205 48.0546 5.25696 47.2095C4.41186 46.3645 3.93709 45.2183 3.93709 44.0231V20.7983H2.2039C1.74423 20.7983 1.30338 20.6157 0.978344 20.2907C0.653307 19.9656 0.470703 19.5248 0.470703 19.0651C0.470703 18.6055 0.653307 18.1646 0.978344 17.8396C1.30338 17.5145 1.74423 17.3319 2.2039 17.3319H3.93709V10.0525ZM42.0673 10.0525C42.0673 8.30577 41.3734 6.63056 40.1383 5.39542C38.9032 4.16028 37.228 3.46639 35.4812 3.46639H13.9896C12.2429 3.46639 10.5677 4.16028 9.33251 5.39542C8.09737 6.63056 7.40348 8.30577 7.40348 10.0525V24.2647H42.0673V10.0525ZM35.1346 41.5966V44.0231C35.1346 44.1597 35.1615 44.2949 35.2137 44.4211C35.266 44.5472 35.3426 44.6619 35.4392 44.7584C35.5357 44.855 35.6504 44.9316 35.7765 44.9839C35.9027 45.0361 36.0379 45.063 36.1745 45.063H41.0274C41.164 45.063 41.2992 45.0361 41.4254 44.9839C41.5516 44.9316 41.6662 44.855 41.7628 44.7584C41.8593 44.6619 41.9359 44.5472 41.9882 44.4211C42.0404 44.2949 42.0673 44.1597 42.0673 44.0231V41.5966H35.1346ZM7.40348 41.5966V44.0231C7.40348 44.1597 7.43038 44.2949 7.48264 44.4211C7.5349 44.5472 7.6115 44.6619 7.70806 44.7584C7.80463 44.855 7.91927 44.9316 8.04543 44.9839C8.1716 45.0361 8.30683 45.063 8.44339 45.063H13.2963C13.4329 45.063 13.5681 45.0361 13.6943 44.9839C13.8205 44.9316 13.9351 44.855 14.0317 44.7584C14.1282 44.6619 14.2048 44.5472 14.2571 44.4211C14.3094 44.2949 14.3363 44.1597 14.3363 44.0231V41.5966H7.40348ZM7.40348 38.1303H42.0673V27.7311H7.40348V38.1303Z" 
                      fill="#2EC4B6"
                    />
                  </svg>
                </div>
                <p class="text-khaki text-base font-medium">
                  En transport <br> en commun
                </p>
              </div>
              <div class="flex flex-col items-center gap-2 md:gap-5">
                <div
                  class="flex group hover:bg-maximum-blue-green duration-150 w-20 h-20 md:w-24 md:h-24 rounded-full border-4 border-maximum-blue-green justify-center items-center p-2 hover:cursor-pointer"
                  :class="`${ deplacement=='voiture' ? 'bg-maximum-blue-green' : 'bg-maastricht-blue'}`"
                  @click="deplacement = 'voiture'"
                >
                  <svg width="72" height="41" viewBox="0 0 72 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                      :class="`${ deplacement=='voiture' ? 'fill-white' : 'fill-maximum-blue-green'}`"  
                      class="group-hover:fill-white duration-150"
                      d="M67.3727 14.0221H59.1066L46.8097 1.57419C46.4461 1.20482 46.0138 0.911938 45.5379 0.712411C45.062 0.512885 44.5517 0.41066 44.0366 0.411628H12.5492C11.9036 0.411437 11.268 0.572573 10.6988 0.880736C10.1295 1.1889 9.64417 1.63456 9.28589 2.17816L0.986171 14.7792C0.802784 15.0591 0.705321 15.3876 0.706059 15.7235V29.334C0.706059 30.3868 1.11922 31.3965 1.85466 32.141C2.5901 32.8855 3.58756 33.3037 4.62763 33.3037H9.83771C10.2234 35.2267 11.2541 36.9555 12.7549 38.1973C14.2558 39.4391 16.1346 40.1175 18.073 40.1175C20.0114 40.1175 21.8902 39.4391 23.3911 38.1973C24.8919 36.9555 25.9226 35.2267 26.3083 33.3037H45.6921C46.0778 35.2267 47.1084 36.9555 48.6093 38.1973C50.1101 39.4391 51.9889 40.1175 53.9273 40.1175C55.8658 40.1175 57.7446 39.4391 59.2454 38.1973C60.7463 36.9555 61.7769 35.2267 62.1626 33.3037H67.3727C68.4128 33.3037 69.4102 32.8855 70.1457 32.141C70.8811 31.3965 71.2943 30.3868 71.2943 29.334V17.9919C71.2943 16.939 70.8811 15.9293 70.1457 15.1849C69.4102 14.4404 68.4128 14.0221 67.3727 14.0221ZM12.0842 4.06662C12.1353 3.98913 12.2044 3.92557 12.2855 3.88156C12.3666 3.83754 12.4572 3.81443 12.5492 3.81426H44.0366C44.1849 3.81489 44.327 3.87505 44.4315 3.98155L54.3531 14.0221H5.52679L12.0842 4.06662ZM18.073 36.7063C17.0758 36.7063 16.101 36.407 15.2718 35.8462C14.4427 35.2853 13.7964 34.4882 13.4148 33.5556C13.0332 32.623 12.9333 31.5967 13.1279 30.6067C13.3224 29.6166 13.8026 28.7072 14.5078 27.9934C15.2129 27.2796 16.1113 26.7935 17.0894 26.5965C18.0674 26.3996 19.0812 26.5007 20.0025 26.887C20.9238 27.2733 21.7113 27.9275 22.2653 28.7668C22.8193 29.6061 23.115 30.5929 23.115 31.6024C23.115 32.9561 22.5838 34.2543 21.6382 35.2114C20.6927 36.1686 19.4102 36.7063 18.073 36.7063ZM53.9273 36.7063C52.9301 36.7063 51.9553 36.407 51.1262 35.8462C50.297 35.2853 49.6507 34.4882 49.2691 33.5556C48.8875 32.623 48.7877 31.5967 48.9822 30.6067C49.1768 29.6166 49.657 28.7072 50.3621 27.9934C51.0672 27.2796 51.9656 26.7935 52.9437 26.5965C53.9217 26.3996 54.9355 26.5007 55.8568 26.887C56.7781 27.2733 57.5656 27.9275 58.1196 28.7668C58.6736 29.6061 58.9694 30.5929 58.9694 31.6024C58.9694 32.9561 58.4381 34.2543 57.4926 35.2114C56.547 36.1686 55.2646 36.7063 53.9273 36.7063ZM67.9329 29.334C67.9329 29.4844 67.8739 29.6286 67.7689 29.735C67.6638 29.8413 67.5213 29.9011 67.3727 29.9011H62.1626C61.7769 27.9781 60.7463 26.2493 59.2454 25.0075C57.7446 23.7657 55.8658 23.0873 53.9273 23.0873C51.9889 23.0873 50.1101 23.7657 48.6093 25.0075C47.1084 26.2493 46.0778 27.9781 45.6921 29.9011H26.3083C25.9226 27.9781 24.8919 26.2493 23.3911 25.0075C21.8902 23.7657 20.0114 23.0873 18.073 23.0873C16.1346 23.0873 14.2558 23.7657 12.7549 25.0075C11.2541 26.2493 10.2234 27.9781 9.83771 29.9011H4.62763C4.47905 29.9011 4.33655 29.8413 4.23149 29.735C4.12643 29.6286 4.0674 29.4844 4.0674 29.334V17.4248H67.3727C67.5213 17.4248 67.6638 17.4845 67.7689 17.5909C67.8739 17.6972 67.9329 17.8415 67.9329 17.9919V29.334Z" 
                      fill="#2EC4B6"
                    />
                  </svg>
                  <!-- <img src="@/src/icone_voiture.svg" alt=""> -->
                </div>
                <p class="text-khaki text-base font-medium">
                  En voiture
                </p>
              </div>
            </div>
            <div 
              v-if="deplacement == 'pied'"
              class="flex flex-col gap-6"
            >
              <p class="text-white font-bold text-2xl md:text-4xl">
                VENIR À PIED
              </p>
              <p class="text-white text-base font-normal md:max-w-lg">
                Trois itinéraires piétons s'offrent à vous pour rejoindre le festival : la montée du Gourguillon, la montée des Chazeaux 
                depuis la rue du Boeuf et la montée Saint-Barthélemy depuis la gare Saint-Paul. <br> <br>
                Gravir la colline à la force de ses muscles, c'est apprécier d'autant plus la vue une fois dans les gradins !
              </p>
            </div>
            <div 
              v-if="deplacement == 'velo'"
              class="flex flex-col gap-6"
            >
              <p class="text-white font-bold text-2xl md:text-4xl">
                VENIR À VÉLO
              </p>
              <p class="text-white text-base font-normal md:max-w-lg">
                Avec le soutien de notre partenaire LPA, deux parkings à vélos sécurisés et gratuits sont installés pendant le festival, 
                les soirs de spectacle. <br> > sur les quais de Saône, à Saint-Jean : un parking à vélos sécurisé situé sur la terrasse du 
                Parking LPA Saint-Jean au niveau de la passerelle du Palais de Justice. <br> > à proximité des théâtres : un parking à vélos 
                sécurisé situé place des Minimes.
              </p>
            </div>
            <div 
              v-if="deplacement == 'bus'"
              class="flex flex-col gap-6"
            >
              <p class="text-white font-bold text-2xl md:text-4xl">
                VENIR EN TRANSPORT EN COMMUN
              </p>
              <p class="text-white text-base font-normal md:max-w-lg">
                Le funiculaire, arrêt Minimes, théâtres romains. <br> Pour gravir la colline et accéder aux théâtres romains, la solution la plus 
                simple est d'emprunter le funiculaire depuis la station Vieux Lyon, direction Saint- Just jusqu'à l'arrêt Minimes, situé 
                face à l'entrée des théâtres. Durant la période du festival, son exploitation est renforcée et prolongée lorsque la programmation 
                l'exige. Alors, n'hésitez plus ! 
              </p>
            </div>
            <div 
              v-if="deplacement == 'voiture'"
              class="flex flex-col gap-6"
            >
              <p class="text-white font-bold text-2xl md:text-4xl">
                VENIR EN VOITURE
              </p>
              <p class="text-white text-base font-normal md:max-w-lg">
                L'accès en voiture et le stationnement aux abords des théâtres sont compliqués et très limités les soirs de spectacle. 
                Pour venir aux Nuits l'esprit tranquille, il est conseillé d'utiliser les parkings relais TCL ou les parkings LPA. 
                Pour un stationnement facilité, il est possible de réserver sa place via parking.lpa.fr.
              </p>
            </div>
          </div>
        </div>
        <div class="grid xl:grid-cols-5 w-full xl:gap-36 gap-6 p-6">
          <div class="flex flex-col gap-6 xl:col-span-3">
            <img 
              class="w-auto lg:max-w-4xl"
              src="@/src/image_5.png" 
              alt=""
            >
            <p class="text-white text-base font-normal italic">
              Édition 2022 des Nuits de Fourvière
            </p>
          </div>
          <div class="flex flex-col gap-12 xl:col-span-2">
            <div>
              <p class="text-white font-normal text-2xl md:text-4xl">
                VENIR AUX NUITS
              </p>
              <p class="text-khaki font-bold text-3xl -mt-5 md:text-5xl">
                HORS LES MURS
              </p>
            </div>
            <div class="flex flex-col gap-9">
              <select 
                name=""
                class="border-2 text-maximum-blue-green border-maximum-blue-green bg-maastricht-blue rounded-full w-80 lg:w-96 px-2 py-1 font-bold"
              >
                <option 
                  value="1"
                  @click="lieu = 'renaissance'"
                >
                  THÉÂTRE LA RENAISSANCE
                </option>
                <option 
                  value="2"
                  @click="lieu = 'celestins'"
                >
                  LES CÉLESTINS, THÉÂTRE DE LYON
                </option>
                <option 
                  value="3" 
                  @click="lieu = 'croix-rousse'"
                >
                  THÉÂTRE DE LA CROIX-ROUSSE
                </option>
                <option 
                  value="4" 
                  @click="lieu = 'lyon'"
                >
                  OPÉRA DE LYON
                </option>
              </select>
              <p 
                v-if="lieu == 'renaissance'"
                class="text-white text-base font-medium"
              >
                ADRESSE : 7 rue Orsel - 69600 Oullins <br> <br> TRANSPORT : <br> > Métro ligne B : Arrêt Gare d'Oullins
              </p>
              <p 
                v-if="lieu == 'celestins'"
                class="text-white text-base font-medium"
              >
                ADRESSE : Place des Célestins, 69002 Lyon <br> <br> TRANSPORTS : <br> > Métro ligne A et D : Arrêt Bellecour <br> > Bus C3, C5, C9, C10, C12, C13, C20
              </p>
              <p 
                v-if="lieu == 'croix-rousse'"
                class="text-white text-base font-medium"
              >
                ADRESSE : Place Joannès Ambre - 69004 Lyon <br> <br> TRANSPORT : <br> > Métro ligne C, Arrêt Croix-Rousse ou Hénon <br> > Bus C13, 38, 33 : Arrêt Hôpital de la Croix-Rousse
              </p>
              <p 
                v-if="lieu == 'lyon'"
                class="text-white text-base font-medium"
              >
                ADRESSE : Place de la Comédie - 69001 Lyon <br> <br> TRANSPORT : <br> > Métro ligne A et C : Arrêt Hôtel de Ville - Louis Pradel <br> > Bus C3, C5, C13, C14, C18, 9, 19, S1, S6, S12, 132, 171
              </p>
            </div>
          </div>
        </div>
        <div class="flex w-full flex-col gap-8 p-6">
          <p class="text-khaki text-5xl font-bold">
            RESTAURATION
          </p>
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-9">
            <div class="flex flex-col gap-4 lg:gap-6">
              <p class="text-white text-4xl font-bold">
                LE BAR DES NUITS
              </p>
              <p class="text-white text-base font-medium max-w-lg">
                L'équipe du bar vous accueille sur la terrasse avant et après chaque spectacle, ainsi que pendant certains concerts. 
                Selon l'événement, un service peut également être assuré dans l'enceinte du théâtre.
              </p>
            </div>
            <div class="flex flex-col gap-4 lg:gap-6">
              <p class="text-white text-4xl font-bold">
                UNE NOUVELLE CARTE
              </p>
              <p class="text-white text-base font-medium max-w-lg">
                Sandwichs variés avec des propositions végétariennes, salades, hot dogs, crêpes, gaufres… vous n'aurez plus qu'à choisir 
                selon votre faim. Côté boissons, nous vous réservons quelques surprises, notamment une nouvelle bière pression et des cocktails.
              </p>
            </div>
            <div class="flex flex-col gap-4 lg:gap-6">
              <p class="text-white text-4xl font-bold">
                DES PRODUITS DE QUALITÉ
              </p>
              <p class="text-white text-base font-medium max-w-lg">
                Pour l'environnement mais aussi pour le goût, nous nous fournissons dans la région et sélectionnons soigneusement nos produits. 
                Notre offre de restauration est majoritairement de saison, locale ou issue de l'agriculture biologique.
              </p>
            </div>
            <div class="flex flex-col gap-4 lg:gap-6">
              <p class="text-white text-4xl font-bold">
                LES GOBELETS CONSIGNÉS
              </p>
              <p class="text-white text-base font-medium max-w-lg">
                Les boissons vous sont servies dans des gobelets réutilisables aux couleurs des Nuits, pour lesquels une consigne de 1 € est 
                demandée. Vous pouvez récupérer ce montant en restituant votre gobelet, qui sera lavé et réutilisé. Ainsi, nous produirons 
                moins de déchets.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      lieu: 'renaissance',
      deplacement: 'pied',
    };
  }
};
</script>