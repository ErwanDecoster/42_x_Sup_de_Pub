<template>
  <div>
    <section class="background w-full h-[95vh]">
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
          </Nuxtlink> > Programmation & Billetterie
        </p>
        <h1 class="uppercase text-8xl text-khaki font-bold w-3/4">
          PROGRAMMATION & BILLETTERIE
        </h1>
        <div class="flex gap gap-6 flex-wrap">
          <div 
            v-for="program in programs" 
            :key="program"
            class="border-2 border-alizarin-crimson text-2xl uppercase font-bold px-6 py-2 cursor-pointer"
            :class="`${ program.filtred ? 'bg-transparent text-alizarin-crimson' : 'bg-alizarin-crimson text-white' }`"
            @click="program.filtred = !program.filtred"
          >
            {{ program.name }}
          </div>
        </div>
      </div>
    </section>
    <section class="bg-maximum-blue-green py-12">
      <div class="mx-auto max-w-screen-xl flex justify-between  px-6">
        <button>Precedent</button>
        <div class="grid grid-cols-5 gap-12 uppercase">
          <div class="space-y-1">
            <p class="text-xl">
              Lundi
            </p>
            <p class="text-7xl font-bold">
              31
            </p>
            <p class="text-xl font-bold">
              MAI
            </p>
          </div>
          <div class="space-y-1">
            <p class="text-xl">
              Mardi
            </p>
            <p class="text-7xl font-bold">
              01
            </p>
            <p class="text-xl font-bold">
              JUIN
            </p>
          </div>
          <div class="space-y-1">
            <p class="text-xl">
              Mercredi
            </p>
            <p class="text-7xl font-bold">
              02
            </p>
            <p class="text-xl font-bold">
              JUIN
            </p>
          </div>
          <div class="space-y-1">
            <p class="text-xl">
              Jeudi
            </p>
            <p class="text-7xl font-bold">
              03
            </p>
            <p class="text-xl font-bold">
              JUIN
            </p>
          </div>
          <div class="space-y-1">
            <p class="text-xl">
              Vendredi
            </p>
            <p class="text-7xl font-bold">
              04
            </p>
            <p class="text-xl font-bold">
              JUIN
            </p>
          </div>
        </div>
        <button>Suivant</button>
      </div>
    </section>
    <section class="pt-12">
      <div
        v-for="program in programs"
        :key="program"
        class="py-4 space-y-16 mx-auto max-w-screen-xl relative"
      >
        <h2 class="text-7xl text-khaki uppercase font-bold">
          {{ program.name }}
        </h2>
        <div class="flex gap-12 overflow-x-scroll relative">
          <div
            v-for="show in program.shows"
            :key="show"
            class="grid gap-7 h-min"
          >
            <div class="relative w-80">
              <img 
                :src="`/${show.imgs[0].url}.jpeg`" 
                alt=""
                class="h-80 w-80 bg-black object-cover"
              >
              <div class="bg-maastricht-blue absolute bottom-0 left-0 h-24 w-24 rounded-tr-full text-white">
                <p class="absolute bottom-3 left-3 text-3xl">
                  {{ show.price }}€
                </p>
              </div>
            </div>
            <div class="flex justify-between">
              <p class="text-xl font-bold text-white">
                {{ show.author }}
              </p>
              <button class="button-secondary ">
                Voir plus
              </button>
            </div>
            <div class="relative z-10 h-36">
              <button 
                class="button-primary-two w-full hover:bg-maastricht-blue absolute"
                @click="show.book = ! show.book" 
              >
                Réserver
              </button>
              <div 
                v-if="show.book"
                class="p-4 space-y-4 absolute bg-zomp right-0 left-0 top-0 pt-14 -z-10 rounded-3xl"
              >
                <select 
                  id=""
                  name="" 
                  class="w-full z-30 border-2 border-maastricht-blue bg-maastricht-blue text-white rounded-full px-2 py-1 font-bold"
                >
                  <option value="select">
                    DATE
                  </option>
                  <option 
                    v-for="date in show.dates"
                    :key="date"
                    :value="date.time"
                  >
                    {{ date.time }}
                  </option>
                </select>
                <div class="flex justify-between">
                  <select 
                    id=""
                    name="" 
                    class="border-2 border-maastricht-blue bg-maastricht-blue text-white rounded-full px-2 py-1 font-bold"
                  >
                    <option value="1">
                      1
                    </option>
                    <option value="2">
                      2
                    </option>
                    <option value="3">
                      3
                    </option>
                    <option value="4">
                      4
                    </option>
                    <option value="5">
                      5
                    </option>
                  </select>
                  <button class="button-primary">
                    Panier
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="absolute z-10 right-0 inset-y-0 h-full w-20 bg-gradient-to-r from-transparent to-maastricht-blue" />
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      programs: [
        {
          filtred: false,
          name: "têtes d'affiche",
          shows: [
            {
              author: "FLORENCE FORESTI",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "florence_foresti",
                },
                {
                  size: 'small',
                  url: "florence_foresti",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "MICHEL POLNAREFF",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "michel_polnareff",
                },
                {
                  size: 'small',
                  url: "michel_polnareff",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "CHRISTINE AND THE QUEENS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "christine_and_the_queens",
                },
                {
                  size: 'small',
                  url: "christine_and_the_queens",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "BENJAMIN BIOLAY",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "benjamin_biolay",
                },
                {
                  size: 'small',
                  url: "benjamin_biolay",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },
        {
          filtred: false,
          name: "MUSIQUE",
          shows: [
            {
              author: "MICHEL POLNAREFF",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "michel_polnareff",
                },
                {
                  size: 'small',
                  url: "michel_polnareff",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "CHRISTINE AND THE QUEENS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "christine_and_the_queens",
                },
                {
                  size: 'small',
                  url: "christine_and_the_queens",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "BENJAMIN BIOLAY",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "benjamin_biolay",
                },
                {
                  size: 'small',
                  url: "benjamin_biolay",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "THE BLACK KEYSE",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "the_black_keyse",
                },
                {
                  size: 'small',
                  url: "the_black_keyse",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },

        {
          filtred: false,
          name: "THÉÂTRE",
          shows: [
            {
              author: "SORCIÈRES",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "sorcieres",
                },
                {
                  size: 'small',
                  url: "sorcieres",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "ISABELLE ADJANI",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "isabelle_adjani",
                },
                {
                  size: 'small',
                  url: "isabelle_adjani",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "LE BEAU MONDE",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "le_beau_monde",
                },
                {
                  size: 'small',
                  url: "le_beau_monde",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "COMP. MARIUS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "comp_marius",
                },
                {
                  size: 'small',
                  url: "comp_marius",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },

        {
          filtred: false,
          name: "CIRQUE",
          shows: [
            {
              author: "BALESTRA",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "balestra",
                },
                {
                  size: 'small',
                  url: "balestra",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "BARO D'EVEL",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "baro_d_evel",
                },
                {
                  size: 'small',
                  url: "baro_d_evel",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "NOFIT STATE CIRCUS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "nofit_state_circus",
                },
                {
                  size: 'small',
                  url: "nofit_state_circus",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },
        {
          filtred: false,
          name: "DANSE",
          shows: [
            {
              author: "COMPAGNIE DCA",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "compagnie_dca",
                },
                {
                  size: 'small',
                  url: "compagnie_dca",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "BEYTNA",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "beytna",
                },
                {
                  size: 'small',
                  url: "beytna",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "MEHDI KERKOUCHE",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "mehdi_kerkouche",
                },
                {
                  size: 'small',
                  url: "mehdi_kerkouche",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "MARÍA PAGÉS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "maria_pages",
                },
                {
                  size: 'small',
                  url: "maria_pages",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },
      ],
    };
  }
};
</script>