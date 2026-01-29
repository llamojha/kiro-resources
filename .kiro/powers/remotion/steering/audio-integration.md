# Audio Integration

## Basic Audio
Add background music or sound effects:

```tsx
import { Audio, staticFile } from 'remotion';

export const VideoWithAudio = () => {
  return (
    <>
      <Audio 
        src={staticFile('background-music.mp3')} 
        volume={0.3}
        startFrom={0}
        endAt={300}
      />
      {/* Your video content */}
    </>
  );
};
```

## Dynamic Volume Control
Animate audio volume over time:

```tsx
import { Audio, staticFile, useCurrentFrame, interpolate } from 'remotion';

export const FadingAudio = () => {
  const frame = useCurrentFrame();
  
  // Fade in first 30 frames, fade out last 30 frames
  const volume = interpolate(
    frame,
    [0, 30, 270, 300],
    [0, 0.5, 0.5, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );
  
  return (
    <Audio 
      src={staticFile('music.mp3')} 
      volume={volume}
    />
  );
};
```

## Audio Visualization
Create audio-reactive visuals:

```tsx
import { useAudioData, visualizeAudio } from '@remotion/media-utils';

export const AudioVisualization = () => {
  const audioData = useAudioData(staticFile('audio.wav'));
  
  if (!audioData) return null;
  
  const visualization = visualizeAudio({
    fps: 30,
    frame: useCurrentFrame(),
    audioData,
    numberOfSamples: 64,
  });
  
  return (
    <div style={{ display: 'flex', alignItems: 'end', height: 200 }}>
      {visualization.map((v, i) => (
        <div
          key={i}
          style={{
            height: v * 100,
            width: 10,
            backgroundColor: 'white',
            margin: 1,
          }}
        />
      ))}
    </div>
  );
};
```

## Audio Timing
Sync audio with visual elements:

```tsx
import { Audio, Sequence, staticFile } from 'remotion';

export const SyncedContent = () => {
  return (
    <>
      {/* Background music throughout */}
      <Audio src={staticFile('background.mp3')} volume={0.2} />
      
      {/* Sound effect at specific moment */}
      <Sequence from={60}>
        <Audio src={staticFile('whoosh.wav')} volume={0.8} />
      </Sequence>
      
      {/* Visual element synced with sound */}
      <Sequence from={60} durationInFrames={30}>
        <AnimatedElement />
      </Sequence>
    </>
  );
};
```

## Best Practices
- Use compressed audio formats (MP3, AAC)
- Keep background music volume low (0.1-0.3)
- Sync sound effects with visual transitions
- Use audio visualization for music videos
- Test audio levels across different devices
- Consider audio ducking for voiceovers
