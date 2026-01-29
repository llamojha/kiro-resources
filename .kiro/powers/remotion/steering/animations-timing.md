# Animations and Timing

## Frame-based Animation
Remotion uses frame-based animation for precise control:

```tsx
import { useCurrentFrame, interpolate } from 'remotion';

export const AnimatedComponent = () => {
  const frame = useCurrentFrame();
  
  // Fade in over first 30 frames
  const opacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  
  // Scale animation
  const scale = interpolate(frame, [0, 60], [0.5, 1], {
    easing: Easing.out(Easing.quad)
  });
  
  return (
    <div style={{ 
      opacity, 
      transform: `scale(${scale})` 
    }}>
      Animated content
    </div>
  );
};
```

## Spring Animations
Use spring() for natural motion:

```tsx
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const SpringComponent = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const scale = spring({
    frame,
    fps,
    config: {
      damping: 200,
      stiffness: 100,
      mass: 0.5,
    },
  });
  
  return (
    <div style={{ transform: `scale(${scale})` }}>
      Spring animation
    </div>
  );
};
```

## Sequencing with Sequence
Control timing of multiple elements:

```tsx
import { Sequence } from 'remotion';

export const SequencedVideo = () => {
  return (
    <>
      <Sequence from={0} durationInFrames={60}>
        <TitleCard />
      </Sequence>
      <Sequence from={50} durationInFrames={120}>
        <MainContent />
      </Sequence>
      <Sequence from={150} durationInFrames={60}>
        <EndCard />
      </Sequence>
    </>
  );
};
```

## Timing Best Practices
- Use 30fps for web content, 60fps for smooth motion
- Plan animations in seconds, convert to frames (seconds × fps)
- Use interpolate() with easing for smooth transitions
- Leverage spring() for natural, bouncy animations
- Sequence overlapping elements for smooth transitions
