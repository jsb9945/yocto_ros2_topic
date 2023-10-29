from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='yocto_ros2_topic', executable='talker', output='screen'),
        launch_ros.actions.Node(
            package='yocto_ros2_topic', executable='listener', output='screen'),
    ])