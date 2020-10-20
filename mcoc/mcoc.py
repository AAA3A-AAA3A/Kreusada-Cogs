from redbot.core import commands, checks, Config
import discord
import random
# from .mdtembed import Embed

class Mcoc(commands.Cog):
  """Mcoc"""
  
  def __init__(self):
    self.config = Config.get_conf(self, 200730042020, force_registration=True)
    
  @commands.group(invoke_without_command=True)
  async def crystal(self, ctx):
    """Chooses a random champion from MCOC."""
    CHAMPS = [
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_abomination.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_aegon.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_agent_venom.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_airwalker.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_angela.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_annihilus.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_antman.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_apocalypse.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_archangel.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_beast_allnew.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_bishop.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_black_bolt.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_black_panther.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_black_panther_cw.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_black_widow.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_black_widow_timely.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_black_widow_movie.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_blade.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_cable.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_captain_america.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_captainamerica_infinitywar.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_capamerica_wwii.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_captain_marvel_movie.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_captain_marvel.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_carnage.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_civilwarrior.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_colossus.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_corvusglaive.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ghost_rider_cosmic.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_crossbones.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_cullobsidian.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_cyclops_90s.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_cyclops.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_daredevil_netflix.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_daredevil.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_darkhawk.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_deadpool.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_deadpool_xforce.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_diablo.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_doctordoom.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_doc_ock.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_doctor_strange.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_brother_voodoo.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_domino.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_dormammu.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_dragonman.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_drax.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ebonymaw.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_electro.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_elektra.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_elsabloodstone.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_emmafrost.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_falcon.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_gambit.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_gamora.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ghost.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ghost_rider.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_deadpool_gold.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_green_goblin.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_groot.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_guardian.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_guillotine.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_guillotine_2099.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_gwenpool.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_havok.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_hawkeye.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_heimdall.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_hela.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_hitmonkey.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_howardmech.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_hulk.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_hulk_ragnarok.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_hulkbuster_movie.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_johnnystorm.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_hyperion.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_iceman.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_invisiblewoman.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_iron_fist.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_iron_fist_white.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_iron_man.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ironman_movie.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ironpatriot.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_joefixit.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_juggernaut.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_kang.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_karnak.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_killmonger.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_groot_king.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_kingpin.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_korg_movie.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_loki.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_longshot.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_luke_cage.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_modok.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_magik.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_magneto.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_magneto_white.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_manthing.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_masacre.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_medusa.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_mephisto.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_mrfantastic.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_mistersinister.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_mojo.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_moleman.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_moonknight.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_karl_mordo.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_morningstar.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_msmarvel.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_msmarvel_kamala.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_mysterio.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_namor.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_nebula.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_nickfury.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_nightthrasher.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_nightcrawler.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_nova.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_wolverine_oldman.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_omegared.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_phoenix.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_deadpool_platinum.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_professorx.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_proximamidnight.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_psylocke.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_punisher.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_punisher_2099.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_quake.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_red_goblin.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_redguardian.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_hulk_red.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_redskull.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_rhino.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_rocket.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_rogue.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ronan.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ronin.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_sabretooth.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_sasquatch.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_scarlet_witch.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_sentinel.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_sentry_current.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_shehulk.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_silversurfer.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_drstrange_realm.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_spidergwen.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_spider_man.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_spiderman_morales.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_spiderman_movie.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_spiderman_stealth.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_spiderman_black.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_squirrelgirl.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_star_lord.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_storm.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_storm_realm.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_storm_realm.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ironman_superior.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_symbiote_supreme.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_taskmaster.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_terrax.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_thanos.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_champion.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_hood.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_thing.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_thor.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_thor_janefoster.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_thor_ragnarok.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_tigra.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ultron.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_ultron_prime.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_colossus_unstoppable.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_venom.png'
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_venomtheduck.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_venompool.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_vision.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_vision_timely.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_vision_movie.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_void_current.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_vulture_movie.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_warmachine.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_warlock.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_wasp.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_winter_soldier.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_wolverine.png',
      'https://vignette.wikia.nocookie.net/marvel-contestofchampions/images/b/b7/Wolverine_%28Weapon_X%29_featured.png/revision/latest?cb=20200601191347',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_x23.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_yellowjacket.png',
      'https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_yondu.png'
      
    ]
    
    await ctx.send(random.choice(CHAMPS))
      
