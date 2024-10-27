# Requirements
import time
import os

# Files path
local = os.getenv('LOCALAPPDATA')
file_path = os.path.join(local, "HarshDoorstop\Saved\Config\WindowsNoEditor\Engine.ini")


# Engine.ini patch
patch = """
[SystemSettings]
r.MotionBlurQuality=0
r.DepthOfFieldQuality=0
r.SceneColorFringeQuality=0
r.Tonemapper.Quality=0
r.Tonemapper.GrainQuantization=0
r.LensFlareQuality=0
r.DefaultFeature.Bloom=0
r.BloomQuality=0
r.EyeAdaptionQuality=0
r.Fog=0
r.VolumetricFog=0
r.VolumetricFog.Jitter=0
r.FastBlurThreshold=0
r.TranslucencyVolumeBlur=0
r.BlurGBuffer=0
r.SSR.Quality=0
FX.MaxCPUParticlesPerEmitter=200
FX.MaxGPUParticlesSpawnedPerFrame=200

[/script/engine.renderersettings]
r.Streaming.Boost=1
r.Streaming.PoolSize=1000
r.Streaming.LimitPoolSizeToVRAM=0
r.Streaming.DefragDynamicBounds=1
r.CreateShadersOnLoad=1
r.Shaders.Optimize=1
r.Shaders.FastMath=1
r.UseShaderCaching=1
r.UseShaderPredraw=1

[/script/engine.inputsettings]
bEnableMouseSmoothing=False

[/script/engine.engine]
bSmoothFrameRate=0
"""


def main():
    print("-- Opration Harsh Doorstop Optimizer --")
    print("Optimization...")
    time.sleep(0.1)
    # print(file_path)
    with open(file_path, "a") as file:
        file.write(patch)
        print("Game patched successfully !")



main()