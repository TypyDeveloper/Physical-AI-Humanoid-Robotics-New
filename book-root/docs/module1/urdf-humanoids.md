# Understanding URDF for Humanoids

URDF (Unified Robot Description Format) is an XML format used in ROS to describe all aspects of a robot. It allows you to define the robot's kinematics (links and joints), visual properties (geometry and colors), and collision properties. For humanoid robots, URDF is essential for accurately representing their complex structure for simulation, visualization, and control.

## Kinematics: Links and Joints

### Links

A **link** represents a rigid body of the robot. This could be a torso, an upper arm, a forearm, or a hand. Each link has associated visual and collision geometries, as well as inertial properties.

### Joints

A **joint** connects two links, defining their relative motion. For humanoid robots, common joint types include:

*   **Revolute**: A single-axis rotational joint (e.g., elbow, knee).
*   **Continuous**: A revolute joint with no upper or lower limits (e.g., a spinning head).
*   **Prismatic**: A linear sliding joint (less common for humanoids but can be used for actuators).
*   **Fixed**: A joint that rigidly attaches two links, meaning no relative motion.

## Visual and Collision Properties

*   **Visual**: Defines the graphical representation of the link. This is what you see in a simulator like Gazebo or RViz.
*   **Collision**: Defines the physical boundaries of the link for collision detection. This is crucial for realistic physics simulation and avoiding self-collisions or collisions with the environment.

## Example: Simple Humanoid Arm Segment

Here's a simplified URDF snippet for an upper arm link and an elbow joint:

```xml
<link name="upper_arm">
  <visual>
    <geometry>
      <cylinder radius="0.05" length="0.3"/>
    </geometry>
    <material name="blue">
      <color rgba="0 0 0.8 1"/>
    </material>
  </visual>
  <collision>
    <geometry>
      <cylinder radius="0.05" length="0.3"/>
    </geometry>
  </collision>
  <inertial>
    <mass value="1.0"/>
    <inertia ixx="0.01" ixy="0" ixz="0" iyy="0.01" iyz="0" izz="0.01"/>
  </inertial>
</link>

<joint name="elbow_joint" type="revolute">
  <parent link="upper_arm"/>
  <child link="forearm"/>
  <origin xyz="0 0 -0.15" rpy="0 0 0"/>
  <axis xyz="0 1 0"/>
  <limit lower="-1.57" upper="1.57" effort="10" velocity="1"/>
</joint>
```

This example defines an `upper_arm` link and an `elbow_joint` that connects it to a `forearm` link (which would be defined elsewhere). The joint is `revolute` (rotational) around the Y-axis, with defined limits.