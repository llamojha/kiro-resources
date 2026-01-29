# Video Compositions

## Composition Structure
Every Remotion video starts with compositions defined in your root file:

```tsx
import { Composition } from 'remotion';
import { MyVideo } from './MyVideo';

export const RemotionRoot = () => {
  return (
    <>
      <Composition
        id="MyVideo"
        component={MyVideo}
        durationInFrames={300}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          title: "Hello World"
        }}
      />
    </>
  );
};
```

## Dynamic Metadata
Use `calculateMetadata` for dynamic composition properties:

```tsx
import { calculateMetadata } from 'remotion';

export const RemotionRoot = () => {
  return (
    <Composition
      id="DynamicVideo"
      component={MyVideo}
      durationInFrames={300}
      fps={30}
      width={1920}
      height={1080}
      calculateMetadata={({ props }) => {
        return {
          durationInFrames: props.duration || 300,
          props: {
            ...props,
            processedTitle: props.title?.toUpperCase()
          }
        };
      }}
    />
  );
};
```

## Best Practices
- Keep compositions focused on single video concepts
- Use descriptive IDs that match your video purpose
- Set appropriate fps (30 for web, 60 for smooth motion)
- Choose resolution based on target platform (1920x1080 for YouTube, 1080x1920 for TikTok)
- Use defaultProps for common configuration
